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
    class Meta:
        model = Hotel
        fields = ('id', 'title', 'description', 'star',)


class HotelRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRule
        fields = ('check_in', 'check_out', 'text')


class HotelCommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.phone_number', read_only=True)
    class Meta:
        model = HotelComment
        fields = ('user', 'comment_body', 'created_time')


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_rooms = HotelRoomSerializer(many=True)
    hotel_features = HotelFeature(many=True)
    hotel_rules = HotelRuleSerializer(many=True)
    hotel_comments = HotelCommentSerializer(many=True)

    class Meta:
        model = Hotel
        fields = (
            'id', 'title', 'average_rating', 'description', 'hotel_features', 'star', 'hotel_rooms', 'hotel_rules',
            'hotel_comments')
