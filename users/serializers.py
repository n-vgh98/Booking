from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone_number')


class ProfileSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source='user.phone_number', read_only=True)
    nationality = serializers.CharField(source='nationality.nationality', read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'user_name', 'email', 'phone_number', 'nationality')


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone_number')

    def create(self, validated_data):
        return super().create(validated_data)


