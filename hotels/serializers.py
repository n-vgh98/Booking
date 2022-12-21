from rest_framework import serializers
from .models import *


class HotelFeature(serializers.ModelSerializer):
    class Meta:
        model = HotelFeature
        fields = ('id', 'title',)


class HotelRoomFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomFeature
        fields = ('id', 'title',)


class HotelRoomSerializer(serializers.ModelSerializer):
    # hotel = serializers.CharField(read_only=True, source='hotel.title')
    room_features = HotelRoomFeatureSerializer(many=True)

    class Meta:
        model = HotelRoom
        fields = ('title', 'description', 'floor', 'breakfast', 'extra_bed', 'room_features')


class HotelSerializer(serializers.ModelSerializer):
    hotel_rooms = HotelRoomSerializer(many=True)
    hotel_features = HotelFeature(many=True)

    class Meta:
        model = Hotel
        fields = ('id', 'title', 'description', 'hotel_features', 'star', 'hotel_rooms',)
