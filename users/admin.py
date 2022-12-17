from django.contrib import admin
from .models import *


class AdminUser(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'date_joined', 'is_active')
    search_fields = ('phone_number', 'date_joined')
    list_filter = ('is_active',)


class AdminNationality(admin.ModelAdmin):
    list_display = ('id', 'country', 'nationality', 'language', 'is_valid')
    search_fields = ('country', 'nationality', 'language')
    list_filter = ('is_valid',)


admin.site.register(User, AdminUser)
admin.site.register(Nationality, AdminNationality)
