import os
import uuid
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

from chat.models.prompt import Prompt
from chat.models.chat import Chat
from chat.models import Response as PromptResponse
from core.models.user import User
from django.core.serializers import serialize


# 1. Refine the serializer to only accept 'prompt'
class PromptSerializer(ModelSerializer):
    class Meta:
        model = Prompt
        fields = ("prompt","created_by")


@api_view(["POST"])
def create_prompt(request):
    serializer = PromptSerializer(data=request.data)
    users = User.objects.all()
    # Serializa los usuarios a JSON
    users_json = serialize('json', users)

# Imprime el JSON
    print(users_json)
    print(users)

    if serializer.is_valid():
        created_by = User.objects.get(id=request.data["created_by"])
        chat = Chat.objects.create(name="New Chat", created_by=created_by)
        prompt_instance = serializer.save(chat=chat)

        api_key = os.getenv("ANTHROPIC_API_KEY")
        anthropic = Anthropic(api_key=api_key)

        try:
            # Corrected API call using messages.create
            response = anthropic.messages.create(
                model="claude-3-haiku-20240307",
                system="You are a helpful assistant.",  # System prompt as parameter
                messages=[
                    {"role": "user", "content": prompt_instance.prompt}  # User message
                ],
                max_tokens=100,  # Correct parameter name
                temperature=0.7
            )
            
            # Extract text content from response
            response_content = response.content[0].text

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Save the extracted response text
        PromptResponse.objects.create(
            prompt=prompt_instance,
            content=response_content
        )

        # Return the response content
        return Response({"response": response_content}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
