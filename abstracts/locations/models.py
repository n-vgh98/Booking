from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=64, unique=True)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "countries"



class Province(models.Model):
    name = models.CharField(max_length=64)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='provinces_of_country')
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [models.UniqueConstraint(fields=('name', 'country'), name='unique_province_country')]

    @property
    def get_country_name(self):
        return self.country.name


class City(models.Model):
    name = models.CharField(max_length=64)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='cities_of_province')
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [models.UniqueConstraint(fields=('name', 'province'), name='unique_city_province')]
        verbose_name_plural = "cities"

    def get_province_name(self):
        return self.province.name

    def get_country_name(self):
        return self.province.country.name


# class AbstractLocation(models.Model):
#
#     city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='location_city')
#     detail_text = models.TextField()
#     is_valid = models.BooleanField(default=True)
#     created_time = models.DateTimeField(auto_now_add=True)
#     modified_time = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         abstract =True
#
#     @property
#     def get_city_name(self):
#         return self.city.name
#
#     def get_province_name(self):
#         return self.city.province.name
#
#     def get_country_name(self):
#         return self.city.province.country.name
