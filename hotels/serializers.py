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


class HotelDailyPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelDailyPrice
        fields = ('price',)


class HotelSpecialPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelSpecialPrice
        fields = ('price',)


class HotelRoomDailyPriceSerializer(serializers.ModelSerializer):
    room_features = HotelRoomFeatureSerializer(many=True)
    price = HotelDailyPriceSerializer(many=True, source='daily_room_price')

    class Meta:
        model = HotelRoom
        fields = ('title', 'description', 'price', 'floor', 'breakfast', 'extra_bed',
                  'room_features')


class HotelImageGallery(serializers.ModelSerializer):
    class Meta:
        model = HotelGalleryImage
        fields = ('path', 'title', 'alt')

class HotelGallery(serializers.ModelSerializer):
    hotel_gallery_images = HotelImageGallery(many=True)
    class Meta:
        model = HotelGallery
        fields = ('name', 'hotel_gallery_images')


class HotelRoomSpecialPriceSerializer(serializers.ModelSerializer):
    # hotel = serializers.CharField(read_only=True, source='hotel.title')
    room_features = HotelRoomFeatureSerializer(many=True)
    price = HotelDailyPriceSerializer(many=True, source='special_room_price')

    class Meta:
        model = HotelRoom
        fields = ('title', 'description', 'price', 'floor', 'breakfast', 'extra_bed',
                  'room_features')

    # def validators(self, fields):
    #     if fields.get('')


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


class HotelDetailDailyPriceSerializer(serializers.ModelSerializer):
    hotel_rooms = HotelRoomDailyPriceSerializer(many=True)
    hotel_features = HotelFeature(many=True)
    hotel_rules = HotelRuleSerializer(many=True)
    hotel_comments = HotelCommentSerializer(many=True)

    class Meta:
        model = Hotel
        fields = (
            'id', 'title', 'average_rating', 'description', 'hotel_features', 'star', 'hotel_rooms',
            'hotel_rules',
            'hotel_comments')


class HotelDetailSpecialPriceSerializer(serializers.ModelSerializer):
    hotel_rooms = HotelRoomSpecialPriceSerializer(many=True)
    hotel_features = HotelFeature(many=True)
    hotel_rules = HotelRuleSerializer(many=True)
    hotel_comments = HotelCommentSerializer(many=True)
    hotel_gallery = HotelGallery(many=True)

    class Meta:
        model = Hotel
        fields = (
            'id', 'title', 'average_rating', 'description', 'hotel_features', 'star', 'hotel_rooms', 'hotel_gallery',
            'hotel_rules',
            'hotel_comments')
