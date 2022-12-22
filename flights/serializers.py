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


class FlightSerializer(serializers.ModelSerializer):
    origin = serializers.CharField(source='origin.name', read_only=True)
    destination = serializers.CharField(source='destination.name', read_only=True)
    airline = serializers.CharField(source='airline.name', read_only=True)

    class Meta:
        model = FlightTicket
        fields = (
            'origin', 'destination', 'airline', 'type', 'flight_class', 'flight_number',
            'luggage_allowance', 'origin_time', 'destination_time')
