from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    msg= serializers.CharField(required=True)
    class Meta:
        model = Chat
        fields = ('msg',)

class ShowChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields=('msg','timestamp')