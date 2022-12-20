from rest_framework import serializers
from .models import *


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'title', 'description', 'star',)


class RoomHotelSerializer(serializers.Serializer):
    hotel = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = RoomHotel
        fields = ('id', 'title', 'hotel', 'floor', 'pluck', 'breakfast', 'extra_bed', 'reserve')
