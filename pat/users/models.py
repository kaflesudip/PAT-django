# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


class IonicUser(models.Model):
    ionic_id = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    sex = models.CharField(
        choices=(('male', 'male'), ('female', 'female')), max_length=255,
        blank=True, null=True
    )
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(null=True)
    tos_accepted = models.BooleanField(default=False)
    tos_accepted_datetime = models.DateField(null=True)
