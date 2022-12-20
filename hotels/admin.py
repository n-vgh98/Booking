from django.contrib import admin
from .models import *

class AdminHotel(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_valid')
    list_filter = ('is_valid',)

class AdminHotelRoom(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_valid', 'hotel')
    list_filter = ('is_valid', )

class AdminHotelFeature(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_valid', 'hotel')
    list_filter = ('is_valid',)

class AdminHotelRoomFeature(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_valid', 'hotel')
    list_filter = ('is_valid',)

class AdminHotelRoomCount(admin.ModelAdmin):
    list_display = ('id', 'hotel', 'room', 'count')


admin.site.register(Hotel, AdminHotel)
admin.site.register(HotelRoom, AdminHotelRoom)
admin.site.register(HotelFeature, AdminHotelFeature)
admin.site.register(HotelRoomFeature, AdminHotelFeature)
admin.site.register(HotelRoomCount, AdminHotelRoomCount)

