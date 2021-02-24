from django.urls import path
from .views import(
    create_or_return_chat,show_chat
)

urlpatterns = [
    path('chat_room/<room_id>',create_or_return_chat, name='chat'),
    path('show/<room_id>',show_chat, name='show'),
]
