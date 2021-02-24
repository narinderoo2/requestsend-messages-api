from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user11')
    name2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user12')
    is_friends = models.BooleanField(default=True)

    def __str__(self):
        return self.name1.username


class Chat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room')
    msg = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.msg
    
    
    
