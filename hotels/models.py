from django.db import models

from abstracts.models import AbstractPlace, AbstractFeature


class Hotel(AbstractPlace):
    star = models.PositiveSmallIntegerField(validators=[1 - 5])

    def rate(self):
        pass


class HotelFeature(AbstractFeature):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_features')


class HotelRoom(AbstractPlace):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_nam="hotel_rooms")
    floor = models.SmallIntegerField()
    count = models.PositiveSmallIntegerField
    # day_price = models.ForeignKey()
    # data_price = models.ForeignKey()
    extra_bed = models.BooleanField(default=False)
    breakfast = models.BooleanField(default=True)
    reserve = models.BooleanField(default=False)


class HotelRoomFeature(AbstractFeature):
    Room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name="room_features")
