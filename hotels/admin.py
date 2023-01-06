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


class AdminHoteRule(admin.ModelAdmin):
    list_display = ('id', 'check_in', 'check_out', 'hotel', 'is_valid')
    list_filter = ('is_valid',)


class AdminHotelComment(admin.ModelAdmin):
    list_display = ('id', 'hotel', 'user', 'status')
    list_filter = ('status',)

    def save_model(self, request, obj, form, change):
        if change and not obj.validated_by and 'status' in form.changed_data:
            obj.validated_by = request.user

        obj.save()


# class AdminHotelLocation(admin.ModelAdmin):
#     list_display = ('id', 'get_hotel_title', 'get_city_name', 'get_province_name', 'get_country_name', 'is_valid')
#     list_filter = ('is_valid',)
# inlines = (AdminHotelCity, )

class AdminHotelDailyPrice(admin.ModelAdmin):
    list_display = ('id', 'day', 'price', 'get_hotel_name', 'room', 'is_valid')
    list_filter = ('is_valid',)

    @admin.display(description='hotel')
    def get_hotel_name(self, obj):
        return obj.room.hotel.title

class AdminHotelSpecialPrice(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'room', 'get_hotel_name', 'is_valid')
    list_filter = ('is_valid',)

    @admin.display(description='hotel')
    def get_hotel_name(self, obj):
        return obj.room.hotel.title


class AdminHotelGallery(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_hotel_name', 'is_valid')
    list_filter = ('is_valid',)

    @admin.display(description='hotel')
    def get_hotel_name(self, obj):
        return obj.hotel.title


class AdminHotelGalleryImage(admin.ModelAdmin):
    list_display = ('id', 'is_valid')
    list_filter = ('is_valid',)

    # @admin.display(description='gallery')
    # def get_gallery_name(self, obj):
    #     return obj.gallery.name

class AdminHotelRoomReservation(admin.ModelAdmin):
    list_display = ('id', 'get_hotel_room_title', 'user', 'status')
    list_filter = ('status', )

    @admin.display(description='room')
    def get_hotel_room_title(self, obj):
        return obj.room.title

class AdminHotelRoomReservationsPassenger(admin.ModelAdmin):
    list_display = ('id', 'national_id')
    search_filed = ('national_id', )

class AdminHotelRate(admin.ModelAdmin):
    list_display = ('id', 'rate', 'user', 'hotel')

admin.site.register(Hotel, AdminHotel)
admin.site.register(HotelRoom, AdminHotelRoom)
admin.site.register(HotelFeature, AdminHotelFeature)
admin.site.register(HotelRoomFeature, AdminHotelRoomFeature)
admin.site.register(HotelRule, AdminHoteRule)
admin.site.register(HotelComment, AdminHotelComment)
admin.site.register(HotelDailyPrice, AdminHotelDailyPrice)
admin.site.register(HotelSpecialPrice, AdminHotelSpecialPrice)
admin.site.register(HotelGallery, AdminHotelGallery)
admin.site.register(HotelGalleryImage, AdminHotelGalleryImage)
admin.site.register(HotelRoomReservation, AdminHotelRoomReservation)
admin.site.register(HotelRoomPassengerReservation, AdminHotelRoomReservationsPassenger)
admin.site.register(HotelRate, AdminHotelRate)
# admin.site.register(HotelLocation, AdminHotelLocation)
