
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('love/', admin.site.urls),
    path('',include('account.urls')),
    path('request/',include('chat.urls')),
    path('chat/',include('message.urls')),
]
