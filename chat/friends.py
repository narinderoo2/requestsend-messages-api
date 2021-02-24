from .models import FriendRequest

def get_friend_request_or_false(sender,reciver):
    try:
        return FriendRequest.objects.get(sender=sender,reciver=reciver, is_active=True)
    except FriendRequest.DoesNotExist:
        return False