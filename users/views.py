import base64
import random

from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .serializers import *
import pyotp
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

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



def otp_generator():
    otp_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNORPQRSTUVWXYZ1234567890@#$%^&*"
    l_otp = [i for i in otp_str]

    return ''.join(random.choices(l_otp, k=6))


class LoginUser(APIView):

    def get(self, request):
        if self.request.data.get("phone_number"):
            phone = self.request.data.get("phone_number")
        else:
            return Response({"phone_number": "phone number is required, please enter"}, status=status.HTTP_400_BAD_REQUEST)
        # try:
        #     User.objects.get(
        #         phone_number=phone)
        # except ObjectDoesNotExist:
        #     User.objects.create(
        #         phone_number=phone,
        #     )
        global otp
        otp = otp_generator()
        cache.set(otp, otp, 60*2)
        cache.add(phone, phone)
        print(cache.get(otp))
        # print(cache.get(phone))

        return Response({"OTP": otp}, status=200)

    # @authentication_classes([JWTAuthentication])
    # @permission_classes(IsAuthenticated)
    def post(self, request, **validated_data):
        phone = request.data.get('phone_number')
        if phone:
            if User.objects.filter(phone_number=phone).exists():
                user = get_object_or_404(User, phone_number=phone)
                # if phone == cache.get(phone):
                # print(cache.get(phone))
                # print(cache.get(otp))
                #check currect otp and phone_otp
                token = get_tokens_for_user(user)
                return Response({"token": token}, status=200)
            print(cache.get(otp))
            return Response({"error": 'not found'}, status=400)
        return Response({"phone": phone}, status=200)

        #
        # serializer = LoginUserSerializer(data=request.data)
        # if serializer in User:
        #     return JsonResponse('hi')
        # if serializer.is_valid():
        #     user = serializer.save()
        #     profile = Profile.objects.create(user=user)
        #     return redirect('user_pofile', profile.id)
        # return JsonResponse(serializer.errors, status=400)
