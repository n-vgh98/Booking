from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics


class HotelLists(generics.ListCreateAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()


class HotelRoom(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HotelRoomSerializer
    queryset = HotelRoom.objects.all()
