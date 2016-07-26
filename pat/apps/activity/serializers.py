from rest_framework import serializers

from .models import ActivityType, Activity


class ActivityTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityType
        fields = ['id', 'name']


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ['lat', 'lon', 'activity_type']
