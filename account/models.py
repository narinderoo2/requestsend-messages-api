import os
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from chat.models import FriendList



class Category(models.Model):
    name = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    profile_name = models.CharField(blank=True,max_length=100)
    country = models.CharField(blank=True,max_length=80)
    state = models.CharField(blank=True,max_length=80)
    adress = models.CharField(blank=True,max_length=500)
    city = models.CharField(blank=True,max_length=80)
    phone = models.IntegerField(blank=True,null=True)
    longitude = models.DecimalField(max_digits=10,decimal_places=6,null=True)
    lattitude = models.DecimalField(max_digits=10,decimal_places=6,null=True)

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.username


class Place(models.Model):
    SATAUS=(
        ('PAID','Paid'),
       ( 'FREE','Free'),
    )
    SATAUS2=(
        ('PROFESSIONAL','Professional'),
        ('LOCAL','Local'),
    )
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    place_name = models.CharField(max_length=400)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    longitude = models.DecimalField(max_digits=10,decimal_places=6,null=True)
    lattitude = models.DecimalField(max_digits=10,decimal_places=6,null=True)
    phone = models.IntegerField(null=True)
    membership = models.CharField(max_length=10,choices=SATAUS,default='Free')
    access = models.CharField(max_length=13,choices=SATAUS2,default='Local')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.place_name




@receiver(post_save, sender=User)
def user_save(sender, instance, **kwargs):
    FriendList.objects.get_or_create(user=instance)