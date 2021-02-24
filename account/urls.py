from django.urls import path
from .views import (
    RegisterList,LoginList,SearchList
)
from .import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register',RegisterList.as_view(),name ='register'),
    path('login',LoginList.as_view(),name='login'),
    path('item',SearchList.as_view(),name='search'),

]
