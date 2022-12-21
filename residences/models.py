from django.db import models
from django.db.models import Avg
from abstracts.locations.models import City
from abstracts.models import *


class ResidenceCategory(models.Model):
    title = models.CharField(max_length=64)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Residence(AbstractPlace):
    category = models.ForeignKey(ResidenceCategory, on_delete=models.NOT_PROVIDED, related_name='residence_category')
    capacity = models.SmallIntegerField(default=1)
    rooms = models.SmallIntegerField(default=0)
    single_bed = models.SmallIntegerField(default=0)
    double_bed = models.SmallIntegerField(default=0)

    @property
    def average_rating(self):
        rate = self.residence_rates.all().aggregate(avg=Avg('rate'))
        return rate.get('avg') or 1


class ResidenceFeature(AbstractFeature):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='residence_features')


class ResidenceRate(AbstractRate):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='residence_rates')

    class Meta:
        constraints = [models.UniqueConstraint(fields=('user', 'residence'), name='unique_user_residence_rate')]


class ResidenceComment(AbstractComment):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='residence_comments')


class ResidenceRule(AbstractRule):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='residence_rules')
