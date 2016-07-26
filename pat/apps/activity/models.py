from django.db import models
from django.conf import settings


class ActivityType(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Activity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    lat = models.FloatField()
    lon = models.FloatField()
    activity_type = models.ForeignKey(ActivityType)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + self.activity_type__name
