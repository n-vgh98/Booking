from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics


class ResidenceList(generics.ListCreateAPIView):
    serializer_class = ResidenceSerializer
    queryset = Residence.objects.filter(is_valid=True)

    def get_queryset(self):
        city = self.request.data.get('city')
        if self.request.method == 'GET':
            query = Residence.objects.filter(city__name=city)
            return query


class ResidenceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResidenceDetailSerializer
    queryset = Residence.objects.filter(is_valid=True)
