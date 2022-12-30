from django.contrib import admin
from .models import *


class AdminResidence(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_location_city', 'get_location_province', 'get_location_country', 'is_valid')
    list_filter = ('is_valid',)

    @admin.display(description='city')
    def get_location_city(self, obj):
        return obj.city.name

    @admin.display(description='province')
    def get_location_province(self, obj):
        return obj.city.province.name

    @admin.display(description='country')
    def get_location_country(self, obj):
        return obj.city.province.country.name


class AdminResidenceCategory(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_filter = ('is_valid',)


class AdminResidenceFeature(admin.ModelAdmin):
    list_display = ('id', 'title', 'residence',)
    list_filter = ('is_valid',)


class AdminResidenceRule(admin.ModelAdmin):
    list_display = ('id', 'check_in', 'check_out', 'residence', 'is_valid')
    list_filter = ('is_valid',)


class AdminResidenceComment(admin.ModelAdmin):
    list_display = ('id', 'residence', 'user', 'status')
    list_filter = ('status',)

    def save_model(self, request, obj, form, change):
        if change and not obj.validated_by and 'status' in form.changed_data:
            obj.validated_by = request.user

        obj.save()


class AdminResidenceDailyPrice(admin.ModelAdmin):
    list_display = ('id', 'day', 'price', 'residence', 'is_valid')
    list_filter = ('is_valid',)


class AdminResidenceSpecialPrice(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'residence', 'is_valid')
    list_filter = ('is_valid',)


class AdminResidenceGallery(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_residence_name', 'is_valid')
    list_filter = ('is_valid',)

    @admin.display(description='residence')
    def get_residence_name(self, obj):
        return obj.residence.title


class AdminResidenceGalleryImage(admin.ModelAdmin):
    list_display = ('id', 'is_valid')
    list_filter = ('is_valid',)

class AdminResidenceReservation(admin.ModelAdmin):
    list_display = ('id', 'get_residence_name', 'user', 'status')
    list_filter = ('status', )

    @admin.display(description='residence')
    def get_residence_name(self, obj):
        return obj.residence.title

class AdminResidenceReservationsPassenger(admin.ModelAdmin):
    list_display = ('id', 'national_id')
    search_filed = ('national_id', )

admin.site.register(Residence, AdminResidence)
admin.site.register(ResidenceCategory, AdminResidenceCategory)
admin.site.register(ResidenceFeature, AdminResidenceFeature)
admin.site.register(ResidenceComment, AdminResidenceComment)
admin.site.register(ResidenceRule, AdminResidenceRule)
admin.site.register(ResidenceDailyPrice, AdminResidenceDailyPrice)
admin.site.register(ResidenceSpecialPrice, AdminResidenceSpecialPrice)
admin.site.register(ResidenceGallery, AdminResidenceGallery)
admin.site.register(ResidenceGalleryImage, AdminResidenceGalleryImage)
admin.site.register(ResidenceReservation, AdminResidenceReservation)
admin.site.register(ResidencePassengerReservation, AdminResidenceReservationsPassenger)
