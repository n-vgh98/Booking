from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from abstracts.locations.models import City
from abstracts.models import *


class Hotel(AbstractPlace):
    star = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def rate(self):
        pass


class HotelFeature(AbstractFeature):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_features')


class HotelRoom(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="hotel_rooms")
    floor = models.SmallIntegerField()
    count = models.PositiveSmallIntegerField()
    # day_price = models.ForeignKey()
    # data_price = models.ForeignKey()
    extra_bed = models.BooleanField(default=False)
    breakfast = models.BooleanField(default=True)
    # reserve = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class HotelRoomFeature(AbstractFeature):
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name="room_features")


class HotelRate(AbstractRate):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_rates')

    class Meta:
        constraints = [models.UniqueConstraint(fields=('user', 'hotel'), name='unique_user_hotel_rate')]


class HotelComment(AbstractComment):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_comments')


class HotelRule(AbstractRule):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_rules')
# class HotelLocation(AbstractLocation):
#     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_location')
#
#     def get_hotel_title(self):
#         return self.hotel.title
#
#     def __str__(self):
#         return self.city.name
