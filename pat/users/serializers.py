from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.hashers import make_password

from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="Already registered with given email. Please Login.")
        ])
    tos_accepted_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = [
            'email', 'password', 'name', 'sex', 'zip_code', 'dob', 'tos_accepted',
            'tos_accepted_date', 'is_full_profile'
        ]

    def create(self, validated_data):
        if 'email' in validated_data:
            validated_data['username'] = validated_data['email']
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

    def save(self, request=None, *args, **kwargs):
        return super(UserSerializer, self).save(*args, **kwargs)
