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
    hotel = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = HotelRoom
        fields = ('id', 'description', 'title', 'hotel', 'floor', 'count', 'breakfast', 'extra_bed',)


class HotelRoomFeatureSerializer(serializers.ModelSerializer):
    room = HotelRoomSerializer

    class Meta:
        model = HotelRoomFeature
        fields = ('id', 'title', 'room')

