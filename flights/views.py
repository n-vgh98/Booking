from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import *
from .models import *
from rest_framework import generics
from users.models import User
from rest_framework.permissions import IsAuthenticated


class FlightsList(generics.ListCreateAPIView):
    serializer_class = FlightSerializer
    queryset = FlightTicket.objects.filter(is_valid=True)

    def get_queryset(self):
        origin = self.request.data.get('origin')
        destination = self.request.data.get('destination')
        date = self.request.data.get('date')
        number = self.request.data.get('number')
        if self.request.method == 'GET':
            query = FlightTicket.objects.filter(is_valid=True, origin__city__name=origin,
                                                destination__city__name=destination,
                                                date_of_departure=date, capacity__gte=number)
            return query


class CreateReservation(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        flight = get_object_or_404(FlightTicket, pk=pk)

        passenger = FlightPassengerReservation()
        passenger.first_name = request.data['firstname']
        passenger.last_name = request.data['lastname']
        passenger.national_id = request.data['national_id']
        passenger.gender = request.data['gender']
        passenger.save(passenger)

        reservation = FlightReservation()
        reservation.flight = flight
        reservation.passenger = passenger
        user = self.request.user
        reservation.user = User.objects.get(id=user.id)

        FlightReservation.save(reservation)

        return Response(status=status.HTTP_201_CREATED)

class FlighttRate(generics.CreateAPIView):
    serializer_class = FlightRateSerializer
    queryset = FlightRate.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        flight = get_object_or_404(FlightTicket, pk=pk)
        rate = FlightRate()
        rate.flight = flight
        user = self.request.user
        rate.user = User.objects.get(id=user.id)
        rate.rate = request.data['rate']
        rate.save(rate)
        return Response(status=status.HTTP_201_CREATED)
