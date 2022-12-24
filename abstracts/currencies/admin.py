from django.contrib import admin
from .models import *


class AdminCurrency(admin.ModelAdmin):
    list_display = ('id', 'code', 'is_valid')
    list_filter = ('is_valid',)


class AdminCurrencyExChangeRate(admin.ModelAdmin):
    list_display = ('id', 'currency_from', 'currency_to', 'rate', 'is_valid')
    list_filter = ('is_valid',)


admin.site.register(Currency, AdminCurrency)
admin.site.register(CurrencyExchangeRate, AdminCurrencyExChangeRate)
