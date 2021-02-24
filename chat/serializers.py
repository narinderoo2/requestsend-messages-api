from rest_framework import serializers
from django.contrib.auth.models import User
from .models import FriendRequest,FriendList

class SendSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset = User.objects.all())
    reciver = serializers.SlugRelatedField(many=False,slug_field='username',queryset=User.objects.all())
    class Meta:
        model = FriendRequest
        fields = ('sender','reciver')



class FriendsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FriendList
        fields = ('friends',)