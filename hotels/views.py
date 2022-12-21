from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *
from rest_framework import generics
from django.shortcuts import render, redirect, get_object_or_404


class HotelLists(generics.ListCreateAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

    def get_queryset(self):
        city = self.request.data.get('city')
        if self.request.method == 'GET':
            query = Hotel.objects.filter(city__name=city)
            return query


class HotelDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()
    #
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
