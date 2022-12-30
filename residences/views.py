from django.shortcuts import render, get_object_or_404

from users.models import User
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


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

@api_view(['POST'])
def create_reservation(request, pk):
    residence = get_object_or_404(Residence, pk=pk)

    passenger = ResidencePassengerReservation()
    passenger.first_name = request.data['firstname']
    passenger.last_name = request.data['lastname']
    passenger.national_id = request.data['national_id']
    passenger.gender = request.data['gender']
    passenger.age = request.data['age']
    passenger.save(passenger)

    reservation = ResidenceReservation()
    reservation.residence = residence
    reservation.passenger = passenger
    reservation.user = User.objects.get(id=1)

    ResidenceReservation.save(reservation)

    return Response(status=status.HTTP_201_CREATED)
