# import os
# import random as r
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.serializers import ModelSerializer
# from rest_framework import status
# from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
# from chat.models.prompt import ConversationDetail



# class ConversationDetailSerializer(ModelSerializer):
#     class Meta:
#         model = ConversationDetail
#         fields = "__all__"
        
# class ConversationDetailView:
    
#     @api_view(["POST"])
#     def create_ConversationDetail(request):
#         serializer = ConversationDetailSerializer(data=request.data)
#         question = request.data['question']
#         if serializer.is_valid():
#             serializer.save()
#             prompt = ConversationDetail.objects.get(question=question)
#             api_key = os.getenv("ANTHROPIC_API_KEY")
#             anthropic = Anthropic(api_key=api_key)
#             prompt = f"{HUMAN_PROMPT} {prompt}{AI_PROMPT}"
#             response = anthropic.completions.create(
#     model="claude-2",  # You can replace with "claude-1" or other supported models
#     max_tokens_to_sample=100,  # Number of tokens to generate
#     prompt=prompt,
#     temperature=0.7,  # Adjust for randomness in the output
# )
            
#             return Response(response, status= status.HTTP_201_CREATED)
#         return Response ("I am Sorry Mate", status= status.HTTP_400_BAD_REQUEST)
        
        