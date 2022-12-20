from rest_framework import serializers
from .models import *


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'title', 'description', 'star',)


class HotelFeature(serializers.ModelSerializer):
    class Meta:
        model = HotelFeature
        fields = ('id', 'title', 'hotel')


class HotelRoomSerializer(serializers.ModelSerializer):
    hotel = serializers.CharField(read_only=True, source='hotel.title')

    class Meta:
        model = HotelRoom
        fields = ('id', 'description', 'hotel', 'title', 'floor', 'count', 'breakfast', 'extra_bed',)


class HotelRoomFeatureSerializer(serializers.ModelSerializer):
    room = HotelRoomSerializer

    class Meta:
        model = HotelRoomFeature
        fields = ('id', 'title', 'room')

