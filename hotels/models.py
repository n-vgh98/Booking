import os

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.exceptions import ValidationError
from abstracts.locations.models import City
from abstracts.models import *
from django.db.models import Avg


class Hotel(AbstractPlace):
    star = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    @property
    def average_rating(self):
        rate = self.hotel_rates.all().aggregate(avg=Avg('rate'))
        return rate.get('avg') or 1


class HotelFeature(AbstractFeature):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_features')


class HotelRoom(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="hotel_rooms")
    count = models.PositiveSmallIntegerField()
    # day_price = models.ForeignKey()
    # date_price = models.ForeignKey()
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

class HotelDailyPrice(AbstractDailyPrice):
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name='daily_room_price')


class HotelSpecialPrice(AbstractSpecialPrice):
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name='special_room_price')

    def save(self, *args, **kwargs):
        today = timezone.now().date()
        try:
            if self.end_date > self.start_date >= today:
                return super(HotelSpecialPrice, self).save(*args, **kwargs)
        except:
            return ValidationError('start_date not valid')


class HotelGallery(AbstractGallery):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_gallery')

    class Meta:
        verbose_name_plural = "Hotel Galleries"


class HotelGalleryImage(AbstractImageGallery):
    gallery = models.ForeignKey(HotelGallery, on_delete=models.CASCADE, related_name='hotel_gallery_images')
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name='hotel_rooms_image', null=True,
                             blank=True)
    path = models.ImageField(upload_to='Hotels/')
    title = models.CharField(max_length=128, null=True, blank=True)
    alt = models.CharField(max_length=128, null=True, blank=True)


class HotelRoomPassengerReservation(AbstractPassenger):
    age = models.PositiveSmallIntegerField(null=True)


class HotelRoomReservation(AbstractReservation):
    room = models.ForeignKey(HotelRoom, on_delete=models.DO_NOTHING, related_name='hotel_room_reservations')
    passenger = models.ForeignKey(HotelRoomPassengerReservation, on_delete=models.CASCADE,
                                  related_name='hotel_room_reservation_passenger')
    start_date = models.DateField()
    end_date = models.DateField()
