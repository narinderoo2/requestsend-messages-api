from django.urls import path
from .views import(
    account_view, send_friend_request,friend_request,
    accept_friend_request,cancel_friend_request
) 

urlpatterns = [
    path('profile/<user_id>',account_view, name='profile'),
    path('send/<int:id>',send_friend_request, name='send'),
    path('show/<int:id>',friend_request, name='show'),
    path('accept/<friend_request>',accept_friend_request, name='accept'),
    path('cancel/<user_id>',cancel_friend_request, name='cancel'),
]
