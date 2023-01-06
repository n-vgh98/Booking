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
from rest_framework import mixins, generics, viewsets


class HotelLists(generics.ListCreateAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.filter(is_valid=True)

    def get_queryset(self):
        city = self.request.data.get('city')
        start_date = self.request.data.get('start_date')
        end_date = self.request.data.get('end_date')
        number = self.request.data.get('number')
        # room_reserved = HotelRoomReservation.objects.filter(start_date=start_date, end_date=end_date,
        #                                                     room__count__gt=number)
        # room_id = []
        # for room in room_reserved:
        #     room_id.append(room.id)
        # print(room_id)
        if self.request.method == 'GET':
            query = Hotel.objects.filter(city__name=city).order_by('-star')
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
        reservation.start_date = request.data['start_date']
        reservation.end_date = request.data['end_date']
        reservation.passenger = passenger
        user = self.request.user
        reservation.user = User.objects.get(id=user.id)
        room_reserved = HotelRoomReservation.objects.filter(start_date=request.data['start_date'],
                                                            end_date=request.data['end_date'])
        room_id = []
        for room in room_reserved:
            room_id.append(room.id)
        if room.id in room_id:
            return Response('this room reserved before you', status=status.HTTP_400_BAD_REQUEST)
        HotelRoomReservation.save(reservation)
        return Response(status=status.HTTP_201_CREATED)


class RateHotel(generics.CreateAPIView):
    serializer_class = HotelRateSerializer
    queryset = HotelRate
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        rate = HotelRate()
        rate.hotel = hotel
        user = self.request.user
        rate.user = User.objects.get(id=user.id)
        rate.rate = request.data['rate']
        rate.save(rate)
        return Response(status=status.HTTP_201_CREATED)


class HotelComment(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = HotelCommentSerializer
    queryset = HotelComment.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]
