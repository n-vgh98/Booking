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


class ResidenceDetailSerializer(serializers.ModelSerializer):
    residence_features = ResidenceFeature(many=True)

    class Meta:
        model = Residence
        fields = ('title', 'capacity', 'description', 'rooms', 'single_bed', 'double_bed', 'residence_features')
