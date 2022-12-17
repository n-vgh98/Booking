from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class ProfileList(generics.ListCreateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer


class UserProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)

    # def get(self, request, pk, *args, **kwargs):
    #     user = get_object_or_404(User, pk=pk)
    #     profile = user.user_profile.get()
    #     print(profile)
    #     return Response(profile)
