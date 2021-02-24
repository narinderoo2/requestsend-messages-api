from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import (
    RegisterSerializer,FilterItemSerializer
)
from django.contrib.auth import authenticate,login
from .models import Profile,Place

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,authentication_classes


from rest_framework import generics,status
from rest_framework.decorators import APIView,api_view,renderer_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from rest_framework.filters import SearchFilter, OrderingFilter

class RegisterList(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        data={}
        if serializer.is_valid():
            account = serializer.save()
            current_user = account
            user = Profile()
            user.name_id = current_user.id
            user.save()

            data['response'] = 'Successfully register a new user'
            data['username'] = account.username
            data['email'] = account.email
            data['password'] = account.password
            token,create = Token.objects.get_or_create(user=account)
            data['token'] = token.key
        else:
            data = serializer.errors
        return Response(data)



class LoginList(generics.GenericAPIView):
    def post(self, request):
        contect = {}
        email= request.POST.get('email')
        password = request.POST.get('password')
        username = User.objects.get(email=email.lower()).username
        account = authenticate(username=username,password=password)
        if account:
            token = Token.objects.get(user=account)
            contect['response']="Succesfully Login"
            contect['token'] = token.key
        else:
            contect['response'] = 'Error'
            contect['error_message'] = 'Invalid creadentails'

        return Response(contect)


from math import radians, cos,sin, asin, sqrt

class SearchList(generics.ListAPIView):
    serializer_class=FilterItemSerializer
    authentication_classes = (TokenAuthentication,)

    # def distance(lat1, lat2, lon1, lon2):
    #     lon1 = radians(lon1)
    #     lon2 = radians(lon2)
    #     lat1 = radians(lat1)
    #     lat2 = radians(lat2)

    #     dlon = lon2 - lon1
    #     dlat = lat2 - lat1

    #     a = sin(dlat / 2) ** 2 +cos(lat1) * cos(lat2) * sin(dlon / 2) **2

    #     c= 2 * asin(sqrt(a))
    #     r= 6371
    #     return (c * r)
    
    # def get(self, request):

        # current_user = request.user

        # print(current_user)
        # check = Profile.objects.get(name_id = current_user.id)

        # print(check)
        # lon1 = Profile.objects.get(longitude=check.longitude)

        # print(lon1)
        # lat1 = Profile.objects.get(lattitude=check.lattitude)
        
        # lon2 = Place.objects.filter(longitude=longitude)
        # lat2 = Place.objects.filter(lattitude=lattitude)


        # queryset=Place.objects.all()
        # filter_backends = (SearchFilter,OrderingFilter)
        # search_fields = ['place_name','membership','access']



    # def get(self, request):

        # current_user = request.user
        # check = Profile.objects.get(name_id = current_user.id)
        # profile1 = Profile.objects.get(longitude=check.longitude)
        # profile2 = Profile.objects.get(lattitude=check.lattitude)
        
        # pnt = str('p')

        # queryset=Place.objects.all()
        # filter_backends = (SearchFilter,OrderingFilter)
        # search_fields = ['place_name','membership','access']

#  pnt = fromstr('POINT(0.002059936523437509 0.00549316405408165)', srid=4326)
#     qs = Shop.objects.filter(location__distance_lte=(pnt,D(km=20)))

