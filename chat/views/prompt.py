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

    # 1. Get the 'created_by' user
    created_by_id = request.data.get("created_by")
    if not created_by_id:
        return Response(
            {"detail": "created_by is required."},
            status=status.HTTP_400_BAD_REQUEST
        )
    created_by = get_object_or_404(User, id=created_by_id)

    # 2. Attempt to get chat_id from request
    chat_id = request.data.get("chat_id")

    if chat_id:
        # Get existing chat; ensure it belongs to the user
        chat = get_object_or_404(Chat, id=chat_id, created_by=created_by)
    else:
        # Create a new chat
        chat = Chat.objects.create(name="New Chat", created_by=created_by)

    # 3. Save the new Prompt
    prompt_instance = serializer.save(chat=chat, created_by=created_by)

    # 4. Fetch conversation history
    history = PromptResponse.objects.select_related(
        "prompt",
        "prompt__chat"
    ).filter(prompt__chat=chat)

    # 5. Build conversation messages
    conversation_messages = [
        {
            "role": "user",
            "content": (
                "You are an AI chatbot designed to provide insights on the stock "
                "status of an inventory based on structured data ..."
            )
        }
    ]

    # **Remove** the get() that caused the error
    # available_products = Inventory.objects.get()  # <-- Remove this line

    # **Use a filtered QuerySet to get all inventory items with quantity > 0**
    available_products = (
        Inventory.objects
        .filter(quantity__gt=0)
        .select_related('product')
        .values_list('quantity', 'product__name')
    )

    # Build a string of available products
    available_products_string = ""
    for quantity, name in available_products:
        available_products_string += f"Quantity: {quantity} - Product: {name}\n"

    conversation_messages.append({
        "role": "user",
        "content": f"The available products are: \n{available_products_string}"
    })

    user_name = created_by.name
    conversation_messages.append({
        "role": "user",
        "content": f"My user name is: {user_name}"
    })

    for item in history:
        # user prompt
        conversation_messages.append({
            "role": "user",
            "content": item.prompt.prompt
        })
        # assistant response
        conversation_messages.append({
            "role": "assistant",
            "content": item.content
        })

    # 6. Append the new user prompt
    conversation_messages.append({
        "role": "user",
        "content": prompt_instance.prompt
    })

    # 7. Prepare the Anthropic client
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return Response(
            {"detail": "Anthropic API key not configured."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    anthropic = Anthropic(api_key=api_key)

    # 8. Call the Anthropic model (adjust model name, messages structure, etc. as needed)
    try:
        response = anthropic.messages.create(
            model="claude-3-haiku-20240307",
            system="You are a helpful assistant.",
            messages=conversation_messages,
            max_tokens=100,
            temperature=0.7
        )
        # The way you extract the response from 'response' may need adjustment
        response_content = response.content[0].text
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # 9. Save the new assistant response
    PromptResponse.objects.create(prompt=prompt_instance, content=response_content)

    # 10. Return the assistant response & chat ID
    return Response(
        {"response": response_content, "chat_id": chat.id},
        status=status.HTTP_201_CREATED
    )

