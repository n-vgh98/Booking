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


admin.site.register(Airport, AdminAirport)
admin.site.register(TerminalAirport, AdminTerminalAirport)
admin.site.register(FlightTicket, AdminFlightTicket)
admin.site.register(AirlineCompany, AdminAirline)
