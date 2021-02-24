from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Room,Chat
from .serializers import ChatSerializer,ShowChatSerializer
from itertools import chain

from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated



@api_view(['POST',])
@permission_classes([IsAuthenticated,])
def create_or_return_chat(request, *args, **kwargs):
    user = request.user
    payload = {}
    room_id = kwargs.get("room_id")
    if room_id:
        check_room = Room.objects.get(pk=room_id)      
        if check_room.name2 == user or check_room.name1==user:
            room = Chat(room=check_room)

            serializer = ChatSerializer(room,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors)

        else:
            payload['response']='not user is correct'
    else:
        return Response({'response':'this user is not in your list'}, status=status.HTTP_404_NOT_FOUND)
    return Response(payload)



@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def show_chat(request, *args, **kwargs):
    user = request.user
    payload = {}
    room_id = kwargs.get("room_id")
    print(room_id)
    if room_id:
        check_room = Room.objects.get(pk=room_id) 
        if check_room.name2 == user or check_room.name1==user:
            chat = Chat.objects.filter(room_id = check_room)
            serializer = ShowChatSerializer(chat,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            payload['response']='You are not a friend'
    else:
        payload['response'] = 'Please check your id'
    return Response(payload)
