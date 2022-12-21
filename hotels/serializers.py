from rest_framework import serializers
from .models import *


class HotelFeature(serializers.ModelSerializer):
    class Meta:
        model = HotelFeature
        fields = ('id', 'title', 'hotel')


class HotelRoomFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomFeature
        fields = ('id', 'title',)


class HotelRoomSerializer(serializers.ModelSerializer):
    # hotel = serializers.CharField(read_only=True, source='hotel.title')
    room_features = HotelRoomFeatureSerializer(many=True)

    class Meta:
        model = HotelRoom
        fields = ('id', 'description', 'title', 'floor', 'count', 'breakfast', 'extra_bed', 'room_features')


class HotelSerializer(serializers.ModelSerializer):
    hotel_rooms = HotelRoomSerializer(many=True)

    class Meta:
        model = Hotel
        fields = ('id', 'title', 'description', 'star', 'hotel_rooms',)
