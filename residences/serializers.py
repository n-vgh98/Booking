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


class ResidenceDetailSerializer(serializers.ModelSerializer):
    residence_features = ResidenceFeature(many=True)
    residence_rules = ResidenceRuleSerializer(many=True)
    residence_comments = ResidenceCommentSerializer(many=True)

    class Meta:
        model = Residence
        fields = (
        'title', 'capacity', 'description', 'average_rating', 'rooms', 'single_bed', 'double_bed', 'residence_features',
        'residence_rules', 'residence_comments')
