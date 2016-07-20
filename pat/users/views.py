# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics
from braces.views import CsrfExemptMixin

from .models import User, IonicUser
from .serializers import IonicUserSerializer

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class FacebookOAuth2AdapterFixed(FacebookOAuth2Adapter):
    def __init__(self):
        pass

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2AdapterFixed


class IonicUserListCreate(generics.ListCreateAPIView, CsrfExemptMixin):
    queryset = IonicUser.objects.all()
    serializer_class = IonicUserSerializer
