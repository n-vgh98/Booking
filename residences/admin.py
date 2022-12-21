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


admin.site.register(Residence, AdminResidence)
admin.site.register(ResidenceCategory, AdminResidenceCategory)
admin.site.register(ResidenceFeature, AdminResidenceFeature)
admin.site.register(ResidenceComment, AdminResidenceComment)
admin.site.register(ResidenceRule, AdminResidenceRule)