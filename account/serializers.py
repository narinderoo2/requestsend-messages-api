from django.contrib.auth.models import User
from .models import Place,Category

from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('username', 'email','password')

    def create(self,validated_data):
        user = User.objects.create(
            username = self.validated_data['username'],
            email = self.validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class FilterItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

