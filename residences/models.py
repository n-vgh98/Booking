from django.core.exceptions import ValidationError
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


class ResidenceDailyPrice(AbstractDailyPrice):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='daily_residence_price')


class ResidenceSpecialPrice(AbstractSpecialPrice):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='special_residence_price')

    def save(self, *args, **kwargs):
        today = timezone.now().date()
        try:
            if self.end_date > self.start_date >= today:
                return super(ResidenceSpecialPrice, self).save(*args, **kwargs)
        except:
            return ValidationError('start_date not valid')


class ResidenceGallery(AbstractGallery):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='residence_gallery')

    class Meta:
        verbose_name_plural = "Residence Galleries"


class ResidenceGalleryImage(AbstractImageGallery):
    gallery = models.ForeignKey(ResidenceGallery, on_delete=models.CASCADE, related_name='residence_gallery_images')
    path = models.ImageField(upload_to='Residence/')
    title = models.CharField(max_length=128, null=True, blank=True)
    alt = models.CharField(max_length=128, null=True, blank=True)


class ResidencePassengerReservation(AbstractPassenger):
    age = models.PositiveSmallIntegerField(null=True, blank=True)


class ResidenceReservation(AbstractReservation):
    residence = models.ForeignKey(Residence, on_delete=models.DO_NOTHING, related_name='residence_reservations')
    passenger = models.ForeignKey(ResidencePassengerReservation, on_delete=models.CASCADE,
                                  related_name='residence_reservation_passenger')
