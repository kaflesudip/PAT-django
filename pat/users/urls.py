# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^rest-auth/facebook/$',
        view=views.FacebookLogin.as_view(),
        name='fb_login'
    ),

    url(
        regex=r'^api/ionic-users-list-create/$',
        view=views.IonicUserListCreate.as_view(),
        name='ionic-users-list-create'
    ),
]
