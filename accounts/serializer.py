from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone']


class KarmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['karma']
