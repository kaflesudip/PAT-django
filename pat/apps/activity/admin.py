from django.contrib import admin

from .models import ActivityType
from .models import Activity

admin.site.register(ActivityType)
admin.site.register(Activity)
