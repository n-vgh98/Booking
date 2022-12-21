from django.contrib import admin
from .models import *


class AdminCountry(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_valid')
    list_filter = ('is_valid',)


class AdminProvince(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_country_name', 'is_valid')
    list_filter = ('is_valid',)


class AdminCity(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_province_name', 'get_country_name', 'is_valid')
    list_filter = ('is_valid',)


admin.site.register(Country, AdminCountry)
admin.site.register(Province, AdminProvince)
admin.site.register(City, AdminCity)
