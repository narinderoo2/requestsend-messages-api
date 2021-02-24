from django.contrib import admin
from .models import Room, Chat

class RoomAdmin(admin.ModelAdmin):
    list_display=['name1','name2','name1_id','id']

    class Meta:
        model = Room

admin.site.register(Room,RoomAdmin)

class ChatAdmin(admin.ModelAdmin):
    list_display=['room','id']
    class Meta:
        model = Chat

admin.site.register(Chat,ChatAdmin)
