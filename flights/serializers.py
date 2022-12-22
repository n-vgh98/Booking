from rest_framework import serializers
from .models import *


class TerminalAirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerminalAirport
        fields = ('number', 'is_valid')


class AirportSerilizer(serializers.ModelSerializer):
    terminal_airport = TerminalAirportSerializer

    class Meta:
        model = Airport
        fields = ('name', 'registration_code', 'terminal_airport')


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightTicket
        fields = ('')
