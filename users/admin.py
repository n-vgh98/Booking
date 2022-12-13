from django.contrib import admin
from .models import *


class AdminUser(admin.ModelAdmin):
    list_display = ('id', 'username', 'date_of_join', 'is_valid')
    search_fields = ('first_name', 'last_name', 'username')
    list_filter = ('is_valid',)


class AdminNationality(admin.ModelAdmin):
    list_display = ('id', 'country', 'nationality', 'language', 'is_valid')
    search_fields = ('country', 'nationality', 'language')
    list_filter = ('is_valid',)


admin.site.register(User, AdminUser)
admin.site.register(Nationality, AdminNationality)
