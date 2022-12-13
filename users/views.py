from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
