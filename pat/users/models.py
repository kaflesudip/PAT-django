# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import datetime

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
    sex = models.CharField(
        choices=(('male', 'male'), ('female', 'female')), max_length=255,
        blank=True, null=True
    )
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(null=True)
    tos_accepted = models.BooleanField(default=False)
    tos_accepted_datetime = models.DateField(null=True)
    is_full_profile = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig = User.objects.get(pk=self.pk)
            print(orig.tos_accepted, self.tos_accepted)
            if not orig.tos_accepted and self.tos_accepted:
                self.tos_accepted_datetime = datetime.datetime.now()
        super(User, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
