from django.db import models
from abstracts.locations.models import City


class AbstractFeature(models.Model):
    title = models.CharField(max_length=128)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractPlace(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True)
    is_valid = models.BooleanField(default=True)
    address_detail = models.TextField(verbose_name='address detail')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    @property
    def get_city_name(self):
        return self.city.name

    @property
    def get_province_name(self):
        return self.city.province.name

    @property
    def get_country_name(self):
        return self.city.province.country.name

