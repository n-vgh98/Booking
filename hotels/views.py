from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import User
from .serializers import *
from .models import *
from rest_framework import generics
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from users.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class HotelLists(generics.ListCreateAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.filter(is_valid=True)
    ordering = ['-star']

    def get_queryset(self):
        city = self.request.data.get('city')
        if self.request.method == 'GET':
            query = Hotel.objects.filter(city__name=city)
            return query


class HotelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.filter(is_valid=True)

    def get_serializer_class(self):
        if Hotel.objects.prefetch_related('hotel_rooms__special_room_price').exists():
            return HotelDetailSpecialPriceSerializer
        return HotelDetailDailyPriceSerializer


class CreateReservation(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        room = get_object_or_404(HotelRoom, pk=pk)

        passenger = HotelRoomPassengerReservation()
        passenger.first_name = request.data['firstname']
        passenger.last_name = request.data['lastname']
        passenger.national_id = request.data['national_id']
        passenger.gender = request.data['gender']
        passenger.age = request.data['age']
        passenger.save(passenger)

        reservation = HotelRoomReservation()
        reservation.room = room
        reservation.passenger = passenger
        user = self.request.user
        reservation.user = User.objects.get(id=user.id)

        HotelRoomReservation.save(reservation)

        return Response(status=status.HTTP_201_CREATED)
