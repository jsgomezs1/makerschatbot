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


# 1. Refine the serializer to only accept 'prompt'
class PromptSerializer(ModelSerializer):
    class Meta:
        model = Prompt
        fields = ("prompt","created_by")


@api_view(["POST"])
def create_prompt(request):
    # 2. Use the refined serializer
    serializer = PromptSerializer(data=request.data)

    if serializer.is_valid():
        
        created_by = User.objects.get(id= request.data["created_by"])
        
        # 3. Create the Chat object
        chat = Chat.objects.create(name="New Chat",created_by=created_by)

        # 4. Save prompt with this chat
        prompt_instance = serializer.save(chat=chat)

        # 5. Prepare the anthropic API call
        api_key = os.getenv("ANTHROPIC_API_KEY")
        anthropic = Anthropic(api_key=api_key)

        # 6. Format the prompt text
        formatted_prompt = f"{HUMAN_PROMPT} {prompt_instance.prompt}{AI_PROMPT}"

        # 7. Call the API
        try:
            response = anthropic.chat.create(
                model="claude-3-haiku-20240307",  # allowed in the Chat/Messages API
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt_instance.prompt},
                ],
                max_tokens_to_sample=100,
                temperature=0.7,
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        # 8. Save the response
        PromptResponse.objects.create(
            prompt=prompt_instance, 
            content=response  # or whatever portion of the response is needed
        )

        # 9. Return the response
        return Response(response, status=status.HTTP_201_CREATED)

    # Handle invalid data
    return Response({"error": "Invalid data provided."}, status=status.HTTP_400_BAD_REQUEST)
