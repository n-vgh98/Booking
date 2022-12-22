from django.db import models
from abstracts.models import AbstractTerminal, AbstractTicket


class Airport(AbstractTerminal):
    registration_code = models.CharField(max_length=64)


class TerminalAirport(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='terminal_airport')
    number = models.PositiveSmallIntegerField(default=1)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


class FlightTicket(AbstractTicket):
    SYSTEMIC = 1
    CHARTER = 0
    TYPE_CHOICES = (
        (SYSTEMIC, 'systemic'),
        (CHARTER, 'charter')
    )

    ECONOMY = 1
    BUSINESS = 2
    FIRST = 3
    FLIGHT_CLASS = (
        (ECONOMY, 'economy'),
        (BUSINESS, 'business'),
        (FIRST, 'first')
    )
    origin = models.ForeignKey(Airport, on_delete=models.DO_NOTHING, related_name='origin_flight_airport')
    destination = models.ForeignKey(Airport, on_delete=models.DO_NOTHING,
                                    related_name='destination_flight_airport')
    type = models.BooleanField(choices=TYPE_CHOICES, default=SYSTEMIC)
    flight_class = models.PositiveSmallIntegerField(choices=FLIGHT_CLASS)