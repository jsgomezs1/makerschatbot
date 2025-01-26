from django.urls import path

from chat.views.prompt import create_prompt





urlpatterns = [ 
               path('claude', create_prompt),
               ]