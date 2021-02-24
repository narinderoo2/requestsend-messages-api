from django.db import models
from django.contrib.auth.models import User


class FriendList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name = 'user')
    friends  = models.ManyToManyField(User,blank=True,related_name='friends')

    def __str__(self):
        return self.user.username

    
    def add_friend(self,account):
        if not account in self.friends.all():
            self.friends.add(account)
            self.save()
    
    
    def mutual_friend(self, account):
        if account in self.friends.all():
            return True
        return False



class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name="sender")
    reciver = models.ForeignKey(User, on_delete=models.CASCADE,related_name="reciver")
    is_active = models.BooleanField(blank=True, null=False,default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username

    def accept(self):
        print('heloo')
        receiver_friend_list = FriendList.objects.get(user=self.reciver)
        print(receiver_friend_list)

        if receiver_friend_list:
            receiver_friend_list.add_friend(self.sender)
            sender_friend_list = FriendList.objects.get(user=self.sender)
            
            if sender_friend_list:
                sender_friend_list.add_friend(self.reciver)
                self.is_active=False
                self.save()

