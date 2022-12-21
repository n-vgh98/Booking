from django.contrib import admin
from .models import *
from abstracts.locations.models import *


# class AdminHotelCity(admin.TabularInline):
#     model = City
#
#     @property
#     def get_city_name(self):
#         return self.city.name


class AdminHotel(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_location_city', 'get_location_province', 'get_location_country', 'is_valid')
    list_filter = ('is_valid',)

    # inlines = (AdminHotelCity, )

    @admin.display(description='city')
    def get_location_city(self, obj):
        return obj.city.name

    @admin.display(description='province')
    def get_location_province(self, obj):
        return obj.city.province.name

    @admin.display(description='country')
    def get_location_country(self, obj):
        return obj.city.province.country.name


class AdminHotelRoom(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_valid', 'hotel')
    list_filter = ('is_valid',)


class AdminHotelFeature(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_valid', 'hotel')
    list_filter = ('is_valid',)


# class HotelName(admin.StackedInline):
#     model = HotelRoom.room


class AdminHotelRoomFeature(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_valid')
    list_filter = ('is_valid',)
    # inlines = (HotelName,)


# class AdminHotelLocation(admin.ModelAdmin):
#     list_display = ('id', 'get_hotel_title', 'get_city_name', 'get_province_name', 'get_country_name', 'is_valid')
#     list_filter = ('is_valid',)
# inlines = (AdminHotelCity, )


admin.site.register(Hotel, AdminHotel)
admin.site.register(HotelRoom, AdminHotelRoom)
admin.site.register(HotelFeature, AdminHotelFeature)
admin.site.register(HotelRoomFeature, AdminHotelRoomFeature)
# admin.site.register(HotelLocation, AdminHotelLocation)
