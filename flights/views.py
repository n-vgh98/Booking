from django.shortcuts import render

from .serializers import *
from .models import *
from rest_framework import generics


class FlightsList(generics.ListCreateAPIView):
    serializer_class = FlightSerializer
    queryset = FlightTicket.objects.filter(is_valid=True)
    # def get_queryset(self):
    #     city = self.request.data.get('city')
    #     if self.request.method == 'GET':
    #         query = Hotel.objects.filter(city__name=city)
    #         return query
