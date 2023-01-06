from django.contrib import admin
from .models import *


class AdminFlightTicket(admin.ModelAdmin):
    list_display = ('id', 'get_origin_name', 'get_destination_name', 'is_valid')
    list_filter = ('origin', 'destination', 'is_valid')

    @admin.display(description='origin')
    def get_origin_name(self, obj):
        return obj.origin.city.name

    @admin.display(description='destination')
    def get_destination_name(self, obj):
        return obj.destination.city.name


class AdminAirport(admin.ModelAdmin):
    list_display = ('id', 'registration_code', 'get_location_city', 'is_valid')
    list_filter = ('is_valid',)

    @admin.display(description='city')
    def get_location_city(self, obj):
        return obj.city.name


class AdminTerminalAirport(admin.ModelAdmin):
    list_display = ('id', 'get_airport_name', 'number', 'is_valid')
    list_filter = ('is_valid', 'number',)

    @admin.display(description='airport')
    def get_airport_name(self, obj):
        return obj.airport.name


class AdminAirline(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_valid')
    list_filter = ('is_valid',)


class AdminFlightReservations(admin.ModelAdmin):
    list_display = ('id', 'origin_airport', 'destination_airport', 'user', 'status')
    list_filter = ('status',)

    @admin.display(description='origin')
    def origin_airport(self, obj):
        return obj.flight.origin.registration_code

    @admin.display(description='destination')
    def destination_airport(self, obj):
        return obj.flight.destination.registration_code


class AdminFlightReservationsPassenger(admin.ModelAdmin):
    list_display = ('id', 'national_id')
    search_filed = ('national_id', )

    # @admin.display(description='reservation')
    # def get_reservation_id(self, obj):
    #     return obj.reservation.id

class AdminFlightRate(admin.ModelAdmin):
    list_display = ('id', 'rate', 'user', 'flight')

class AdminFlightComment(admin.ModelAdmin):
    list_display = ('id', 'flight', 'user', 'status')
    list_filter = ('status',)

    def save_model(self, request, obj, form, change):
        if change and not obj.validated_by and 'status' in form.changed_data:
            obj.validated_by = request.user

        obj.save()


admin.site.register(Airport, AdminAirport)
admin.site.register(TerminalAirport, AdminTerminalAirport)
admin.site.register(FlightTicket, AdminFlightTicket)
admin.site.register(AirlineCompany, AdminAirline)
admin.site.register(FlightReservation, AdminFlightReservations)
admin.site.register(FlightPassengerReservation, AdminFlightReservationsPassenger)
admin.site.register(FlightRate, AdminFlightRate)
admin.site.register(FlightComment, AdminFlightComment)
