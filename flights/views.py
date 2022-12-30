from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework import generics
from users.models import User

class FlightsList(generics.ListCreateAPIView):
    serializer_class = FlightSerializer
    queryset = FlightTicket.objects.filter(is_valid=True)

    def get_queryset(self):
        origin = self.request.data.get('origin')
        destination = self.request.data.get('destination')
        date = self.request.data.get('date')
        if self.request.method == 'GET':
            query = FlightTicket.objects.filter(origin__city__name=origin, destination__city__name=destination,
                                                date_of_departure=date, capacity__gt=0)
            return query


# class FlightPassenger(RetrieveAPIView, CreateAPIView):
#     serializer_class = FlightSerializer
#     queryset = FlightTicket.objects.filter(is_valid=True)

@api_view(['POST'])
def create_reservation(request):
    flight = FlightTicket.objects.get(id=request.data['flight_number'])

    passenger = FlightPassengerReservation()
    passenger.first_name = request.data['firstname']
    passenger.last_name = request.data['lastname']
    passenger.national_id = request.data['national_id']
    passenger.gender = request.data['gender']
    passenger.save(passenger)

    reservation = FlightReservation()
    reservation.flight = flight
    reservation.passenger = passenger
    reservation.user = User.objects.get(id=1)

    FlightReservation.save(reservation)
    flight.capacity = 1

    return Response(status=status.HTTP_201_CREATED)
