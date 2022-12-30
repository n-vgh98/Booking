from rest_framework import serializers
from .models import *


class TerminalAirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerminalAirport
        fields = ('number', 'is_valid')


class AirportSerializer(serializers.ModelSerializer):
    terminal_airport = TerminalAirportSerializer

    class Meta:
        model = Airport
        fields = ('name', 'registration_code', 'terminal_airport')


class AirlineCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AirlineCompany
        fields = ('name',)


class PassengerReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightPassengerReservation
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    origin = serializers.CharField(source='origin.city.name', read_only=True)
    destination = serializers.CharField(source='destination.city.name', read_only=True)
    airline = serializers.CharField(source='airline.name', read_only=True)
    flight_class = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    def get_flight_class(self, obj):
        return obj.get_flight_class_display()

    def get_type(self, obj):
        return obj.get_type_display()

    class Meta:
        model = FlightTicket
        fields = (
            'origin', 'destination', 'capacity', 'price', 'airline', 'type', 'flight_class', 'flight_number',
            'luggage_allowance', 'date_of_departure', 'time_of_departure')


class FlightPassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightPassengerReservation
        fields = '__all__'


class FlightReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightReservation
        fields = '__all__'

# class FlightReservationSerializer(serializers.ModelSerializer):
#     # flight_reservation_passengers = PassengerReservationSerializer(many=True)
#     flight_reservations = FlightSerializer(many=True)
#
#     class Meta:
#         model = FlightReservation
#         fields = ('flight_reservations',)
