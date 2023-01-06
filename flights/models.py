from django.db import models
from abstracts.models import AbstractTerminal, AbstractTicket, AbstractPassenger, AbstractReservation, AbstractRate, \
    AbstractComment


class Airport(AbstractTerminal):
    registration_code = models.CharField(max_length=64)


class TerminalAirport(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='terminal_airport')
    number = models.PositiveSmallIntegerField(default=1)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


class AirlineCompany(models.Model):
    name = models.CharField(max_length=64)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


# class Flight()

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
    airline = models.ForeignKey(AirlineCompany, on_delete=models.CASCADE, related_name='ticket_airline')
    type = models.BooleanField(choices=TYPE_CHOICES, default=SYSTEMIC)
    flight_class = models.PositiveSmallIntegerField(choices=FLIGHT_CLASS)
    flight_number = models.PositiveSmallIntegerField()
    luggage_allowance = models.PositiveSmallIntegerField(default=20)


class FlightPassengerReservation(AbstractPassenger):
    # reservation = models.ForeignKey(FlightReservation, on_delete=models.CASCADE,
    #                                 related_name='flight_reservation_passengers')
    date_birth = models.DateField(null=True, blank=True)


class FlightReservation(AbstractReservation):
    flight = models.ForeignKey(FlightTicket, on_delete=models.DO_NOTHING, related_name='flight_reservations')
    passenger = models.ForeignKey(FlightPassengerReservation, on_delete=models.CASCADE,
                                     related_name='flight_reservation_passenger')

    def save(self, *args, **kwargs):
        capacity = self.flight.capacity
        print(capacity)
        capacity -= 1
        FlightTicket.objects.update(capacity=capacity)
        print(capacity)
        return super(FlightReservation, self).save(*args, *kwargs)


class FlightRate(AbstractRate):
    flight = models.ForeignKey(FlightTicket, on_delete=models.CASCADE, related_name='flight_rates')

    class Meta:
        constraints = [models.UniqueConstraint(fields=('user', 'flight'), name='unique_user_flight_rate')]


class FlightComment(AbstractComment):
    flight = models.ForeignKey(FlightTicket, on_delete=models.CASCADE, related_name='flight_comments')
