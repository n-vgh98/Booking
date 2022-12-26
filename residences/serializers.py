from rest_framework import serializers
from .models import *


class ResidenceFeature(serializers.ModelSerializer):
    class Meta:
        model = ResidenceFeature
        fields = ('title', 'is_valid')


class ResidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residence
        fields = ('title', 'capacity', 'description', 'rooms', 'single_bed', 'double_bed',)


class ResidenceRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidenceRule
        fields = ('check_in', 'check_out', 'text')


class ResidenceCommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.phone_number', read_only=True)

    class Meta:
        model = ResidenceComment
        fields = ('user', 'comment_body', 'created_time')


class ResidenceDailyPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidenceDailyPrice
        fields = ('price',)


class ResidenceSpecialPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidenceSpecialPrice
        fields = ('price',)

class ResidenceImageGallery(serializers.ModelSerializer):
    class Meta:
        model = ResidenceGalleryImage
        fields = ('path', 'title', 'alt')

class ResidenceGallery(serializers.ModelSerializer):
    residence_gallery_images = ResidenceImageGallery(many=True)
    class Meta:
        model = ResidenceGallery
        fields = ('name', 'residence_gallery_images')


class ResidenceDetailSerializer(serializers.ModelSerializer):
    residence_features = ResidenceFeature(many=True)
    residence_rules = ResidenceRuleSerializer(many=True)
    residence_comments = ResidenceCommentSerializer(many=True)
    daily_residence_price = ResidenceDailyPriceSerializer(many=True)
    special_residence_price = ResidenceSpecialPriceSerializer(many=True)
    residence_gallery = ResidenceGallery(many=True)

    class Meta:
        model = Residence
        fields = (
            'title', 'capacity', 'description', 'daily_residence_price', 'special_residence_price', 'average_rating',
            'residence_gallery', 'rooms', 'single_bed', 'double_bed', 'residence_features',
            'residence_rules', 'residence_comments')
