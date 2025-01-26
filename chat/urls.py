from django.urls import path

from chat.chat import ConversationDetailView



urlpatterns = [ 
               path('claude', ConversationDetailView.create_ConversationDetail),
               ]