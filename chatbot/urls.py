from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('messages/', views.chat_messages, name='chat_messages'),
]
