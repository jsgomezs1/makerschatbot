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


class PromptSerializer(ModelSerializer):
    """
    Only accepts 'prompt'. If your model requires `created_by` as part of
    the payload, you can include it in fields or handle it in the view.
    """
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
    #    (Keep your big "You are an AI chatbot..." in the system parameter,
    #     or store it in the conversation as a system message.)
    conversation_messages = []

    # A) If you want a single system message with your big instruction:
    #    You can either pass it directly to Anthropic as `system=...`
    #    or do it as a "system" role message in the conversation. 
    #    We'll illustrate "system" role in the conversation:
    conversation_messages.append({
        "role": "assistant",
        "content": (
            "You are an AI chatbot designed to provide insights on the stock "
            "status of an inventory based on structured data. The inventory includes "
            "stakeholders, brands, tags, product types, products, and so on. "
            "You will answer questions about available stock levels, brand inventory, "
            "and so forth. Be concise and do not add unrelated info."
        )
    })

    # B) Provide inventory data as an assistant message so Claude treats it like
    #    known context, not user instructions:
    
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

    # Let the assistant "say" the inventory for context:
    conversation_messages.append({
        "role": "assistant",
        "content": (
            "Here is the current inventory:\n"
            f"{inventory_text}"
        )
    })

    # C) (Optional) If the user literally typed their name: 
    #    That can be a user message:
    user_name = created_by.name
    conversation_messages.append({
        "role": "user",
        "content": f"My user name is: {user_name}"
    })

    # D) Now append the existing conversation history with correct roles
    for item in history:
        # item.prompt.prompt = what the user said
        conversation_messages.append({
            "role": "user",
            "content": item.prompt.prompt
        })
        # item.content = the AI's response
        conversation_messages.append({
            "role": "assistant",
            "content": item.content
        })

    # E) Append the new user prompt
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
            # You could also do system="You are a helpful assistant" here, or skip if
            # you used a system role message in conversation_messages
            messages=conversation_messages,
            max_tokens=200,
            temperature=0.7
        )
        # Adjust how you extract the text depending on how the library returns it
        response_content = response.content[0].text
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # 7. Save the new assistant response
    PromptResponse.objects.create(prompt=prompt_instance, content=response_content)

    # 8. Return the assistant response & chat ID
    return Response({"response": response_content, "chat_id": chat.id},
                    status=status.HTTP_201_CREATED)


