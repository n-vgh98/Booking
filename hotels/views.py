from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from .serializers import *
from .models import *
from rest_framework import generics
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
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

    # def get_queryset(self, *args):
    #     # hotel_id = self.kwargs['pk']
    #     # room_id = HotelRoom.objects.filter(hotel__id=hotel_id)
    #     if Hotel.objects.prefetch_related('hotel_rooms__special_room_price'):
    #         return Hotel.objects.prefetch_related('hotel_rooms__special_room_price')
    #     return Hotel.objects.prefetch_related('hotel_rooms__daily_room_price')
    #     # try:
        #     special_price =
        #     return special_price
        # except:
        #     daily_price =
        #     return daily_price
        # return Hotel.objects.filter(id=hotel_id)

@api_view(['POST'])
def create_reservation(request, pk):
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
    reservation.user = User.objects.get(id=1)

    HotelRoomReservation.save(reservation)

    return Response(status=status.HTTP_201_CREATED)
