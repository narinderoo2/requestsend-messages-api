from django.shortcuts import render
from django.contrib.auth.models import User
from .models import FriendList, FriendRequest
from .serializers import SendSerializer,FriendsSerializer
from .friends import get_friend_request_or_false
from .friend_request_status import FriendRequestStatus
from message.models import Room

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics,status


from rest_framework.decorators import permission_classes,authentication_classes



@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def account_view(request,*args, **kwargs):
    context = {}
    user_id = kwargs.get('user_id')
    
    try:
        account = User.objects.get(pk=user_id)
        print(account)
    except:
        return Response({"msg":"something was wrong"})
    
    if account:
        try:
            friend_list = FriendList.objects.get(user=account)
        except FriendList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        friends = friend_list.friends.all()
        # context['friends'] =f"{friends}"
        if friends:

            serializer = FriendsSerializer(friends, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            context['response'] = 'have no friends in your list'
    else:
        context['response'] = 'have not request'
    return Response(context)

        # #show for freont end 
        # is_self = True
        # is_friend = False
        # # request_send = FriendRequestStatus.NO_REQUEST_SENT.value
        # # friend_request = None
        # user = request.user
        # # if user !=account:  # is_authenticated
        # #     is_self = False
        # #     if friends.filter(pk=user.id):
        # #         is_friend = True
        # #     else:
        # #         is_friend = False

        # #         #case 1 = request has been send from then to you

        # #         if get_friend_request_or_false(sender=account, reciver = user) != False:
        # #             request_sent = FriendRequestStatus.THEN_SENT_TO_YOU.value
        # #             context['pending friend_request_id'] = get_friend_request_or_false(sender=account, reciver=user).id

        # #         #case2= request has been send from you 2 then

        # #         elif get_friend_request_or_false(sender=account,reciver = user) != False:
        # #             request_sent = FriendRequestStatus.YOU_SENT_TO_THEM.value

        # #         #case 3= no request has been send 
        # #         else:
        # #             request_sent = FriendRequestStatus.NO_REQUEST_SENT.value


        
        # if not user:  #is_authenticated
        #     is_self = False
        # else:
        #     try:
        #         friend_request = FriendRequest.objects.filter(reciver=user, is_active=True)
        #     except :
        #         pass
        #     return Response({"response":"request is pendding"})
        
    # return Response(context)

        

""" any user request send 
but this condition only user send request
    in case your request is accept, so next time again friend request you can send.
    (create a profile fuction, it can decide send request or not )
    """

@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def send_friend_request(request,id):
    user = request.user
    contect = {}
    try:
        receiver = User.objects.get(pk=id)
        if receiver:
            friend_request = FriendRequest.objects.filter(sender=user,reciver=receiver)
            try :
                for ps in friend_request:
                    if ps.is_active:
                        return Response({"msg":"You alredy request send"})
                
                friend_request = FriendRequest(sender=user, reciver=receiver)
                friend_request.save()
                contect['response'] = 'success'

            except FriendRequest.DoesNotExist:
                contect['respose'] = f" Please check user id {str(e)}" 
        else:
            contect['response'] = "Not correct"
    except Exception as e:
        contect['response'] =  "Not correct user"

    return Response(contect)


"""first user check request of other user (receve request)

    user check all request of pending request 
    pending request is (is activve True) """
@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def friend_request(request, id):
    context = {}
    user = request.user
    account = User.objects.get(pk=id)
    if account == user:
        try:
            friend_request_show = FriendRequest.objects.filter(reciver= account, is_active=True)
            print(friend_request_show)
        except FriendRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SendSerializer(friend_request_show, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response({"msg":"you can't view another user friend request"})
    return Response(context)


# request accept user one time one request accept, but this field work with model id not a user id
#condition apply:- is active user, so request accept
@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def accept_friend_request(request, *args, **kwargs):
    user = request.user
    contect= {}
    friend_request_id = kwargs.get("friend_request")
    if friend_request_id:
        friend_request = FriendRequest.objects.get(pk=friend_request_id)
        if friend_request.reciver == user:
            if friend_request:
                notification = friend_request.accept()
                contect['response'] = "friend request accpet"

                #new models data save in auto
                user1,created = Room.objects.get_or_create(name1=user, name2=friend_request.sender)
                user1.save()
                contect['succes'] = 'you can send message your frieds'

            else:
                contect['response'] = "something went wrong"
        else:
            contect['response']="That is not your request"
    else:
        contect['response'] = 'unable'
    return Response(contect)



# you have any request of unknow user you can cancel request with the help of that's logic
@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def cancel_friend_request(request,*args, **kwargs):
    user = request.user
    contect = {}
    user_id = kwargs.get("user_id")
    print(user_id)
    if user_id:
        friend_request = FriendRequest.objects.get(pk=user_id)
        if friend_request.reciver == user:
            if friend_request:
               friend_request.delete()
               contect['response']="Friend request canceel"
            else:
                contect['response'] = "Wring"
        else:
            contect['response'] = "this is not your friend request"
    else:
        payloas['response']="unable"

    return Response(contect)


