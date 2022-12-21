from django.db import models

from abstracts.locations.models import City
from abstracts.models import AbstractPlace, AbstractFeature


class ResidenceCategory(models.Model):
    title = models.CharField(max_length=64)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Residence(AbstractPlace):
    category = models.ForeignKey(ResidenceCategory, on_delete=models.NOT_PROVIDED, related_name='residence_category')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='residence_city')
    capacity = models.SmallIntegerField(default=1)
    rooms = models.SmallIntegerField(default=0)
    single_bed = models.SmallIntegerField(default=0)
    double_bed = models.SmallIntegerField(default=0)

    def rate(self):
        pass


class ResidenceFeature(AbstractFeature):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='residence_features')
