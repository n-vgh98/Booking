from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView

from .serializers import *
from .models import *
from rest_framework import generics


class FlightsList(generics.ListCreateAPIView):
    serializer_class = FlightSerializer
    queryset = FlightTicket.objects.filter(is_valid=True)

    def get_queryset(self):
        origin = self.request.data.get('origin')
        destination = self.request.data.get('destination')
        if self.request.method == 'GET':
            query = FlightTicket.objects.filter(origin__city__name=origin, destination__city__name=destination)
            return query


class FlightPassenger(RetrieveAPIView):
    # serializer_class = FlightSerializer
    # queryset = FlightTicket.objects.filter(is_valid=True)

    def get(self, request, *args, **kwargs):
        queryset = FlightTicket.objects.filter(is_valid=True)
        serializers_class = FlightSerializer(queryset)
        return serializers_class.data
