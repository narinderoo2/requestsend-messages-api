from django.contrib import admin
from .models import Profile,Category,Place

class ProfileAdmin(admin.ModelAdmin):
    list_display=['name','category','profile_name']



admin.site.register(Category)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Place)


