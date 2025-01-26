import os
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from anthropic import Anthropic

from chat.models.prompt import Prompt
from chat.models.chat import Chat
from chat.models import Response as PromptResponse
from core.models.user import User
from inventory.models.inventory import Inventory
from inventory.models.user_product import UserProduct

# Assuming your ProductTag model is something like:
# class ProductTag(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

# And Product -> Brand -> Stakeholder relationships are set up accordingly.

from django.db.models import F
from inventory.models.product_tag import ProductTag  # or wherever it is


class PromptSerializer(ModelSerializer):
    class Meta:
        model = Prompt
        fields = ("prompt",)


@api_view(["POST"])
@transaction.atomic
def create_prompt(request):
    serializer = PromptSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 1. Validate user (created_by)
    created_by_id = request.data.get("created_by")
    if not created_by_id:
        return Response({"detail": "created_by is required."},
                        status=status.HTTP_400_BAD_REQUEST)
    created_by = get_object_or_404(User, id=created_by_id)

    # 2. Get or create a Chat
    chat_id = request.data.get("chat_id")
    if chat_id:
        chat = get_object_or_404(Chat, id=chat_id, created_by=created_by)
    else:
        chat = Chat.objects.create(name="New Chat", created_by=created_by)

    # 3. Save the new Prompt
    prompt_instance = serializer.save(chat=chat, created_by=created_by)

    # 4. Fetch conversation history
    history = PromptResponse.objects.select_related(
        "prompt", "prompt__chat"
    ).filter(prompt__chat=chat)

    # 5. Build conversation messages
    conversation_messages = []

    # System instructions or big context
    conversation_messages.append({
        "role": "assistant",
        "content": (
            "You are an AI chatbot designed to provide insights on the stock "
            "status of an inventory, as well as the relationships between tags, products, "
            "brands, and stakeholders (companies). You will answer questions about available "
            "stock levels, brand inventory, product tags, and more. Be concise."
        )
    })

    # -----------------------------------------------------
    # A) Available products in inventory (existing example)
    # -----------------------------------------------------
    available_products_qs = (
        Inventory.objects
        .filter(quantity__gt=0)
        .select_related('product')
        .values_list('quantity', 'product__name')
    )

    if available_products_qs.exists():
        inventory_lines = []
        for quantity, product_name in available_products_qs:
            inventory_lines.append(f"{product_name}: {quantity}")
        inventory_text = "\n".join(inventory_lines)
    else:
        inventory_text = "No products currently in stock."

    conversation_messages.append({
        "role": "assistant",
        "content": (
            "Here is the current inventory:\n"
            f"{inventory_text}"
        )
    })

    # -----------------------------------------------------
    # B) Tag–Product–Brand–Company listing (NEW part)
    # -----------------------------------------------------
    tagged_products_qs = (
        ProductTag.objects
        .select_related("tag", "product__brand__stakeholder")  # so we don't hit the DB repeatedly
        .values(
            tag_name=F("tag__name"),
            product_name=F("product__name"),
            brand_name=F("product__brand__name"),
            company_name=F("product__brand__stakeholder__name")
        )
    )

    if tagged_products_qs.exists():
        lines = []
        for row in tagged_products_qs:
            lines.append(
                f"Tag: {row['tag_name']}, "
                f"Product: {row['product_name']}, "
                f"Brand: {row['brand_name']}, "
                f"Company: {row['company_name']}"
            )
        tag_product_text = "\n".join(lines)
    else:
        tag_product_text = "No tag–product–brand data found."

    # Include this as context for the AI:
    conversation_messages.append({
        "role": "assistant",
        "content": (
            "Here is the current tag–product–brand–company mapping:\n"
            f"{tag_product_text}"
        )
    })

    # (Optional) Some user-provided info
    user_name = created_by.name
    conversation_messages.append({
        "role": "user",
        "content": f"My user name is: {user_name}"
    })

    # D) Insert prior conversation history
    for item in history:
        conversation_messages.append({
            "role": "user",
            "content": item.prompt.prompt
        })
        conversation_messages.append({
            "role": "assistant",
            "content": item.content
        })

    # E) The new user prompt
    conversation_messages.append({
        "role": "user",
        "content": prompt_instance.prompt
    })

    # 6. Call Anthropic
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return Response(
            {"detail": "Anthropic API key not configured."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    anthropic = Anthropic(api_key=api_key)

    try:
        response = anthropic.messages.create(
            model="claude-3-haiku-20240307",
            messages=conversation_messages,
            max_tokens=200,
            temperature=0.7
        )
        # Depending on the library version, adapt how you access `response_content`
        response_content = response.content[0].text
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # 7. Save new assistant response
    PromptResponse.objects.create(prompt=prompt_instance, content=response_content)

    # 8. Return the assistant response & chat ID
    return Response({"response": response_content, "chat_id": chat.id},
                    status=status.HTTP_201_CREATED)
