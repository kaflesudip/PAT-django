from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from .serializers import ActivityTypeSerializer, ActivitySerializer
from .models import ActivityType, Activity


class ActivityTypeList(generics.ListAPIView):
    serializer_class = ActivityTypeSerializer
    queryset = ActivityType.objects.all()


class ActivityListCreate(generics.ListCreateAPIView):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
