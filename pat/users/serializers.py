from rest_framework import serializers
from .models import IonicUser


class IonicUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = IonicUser
        fields = [
            'ionic_id', 'email', 'sex', 'zip_code', 'dob', 'tos_accepted',
            'tos_accepted_datetime'
        ]
