# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    # URL pattern for the UserListView

    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),

    # URL pattern for the UserRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the UserDetailView
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the UserUpdateView
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),


    url(
        regex=r'^rest-auth/facebook/$',
        view=views.FacebookLogin.as_view(),
        name='fb_login'
    ),

    url(
        regex=r'^rest-auth/google/$',
        view=views.GoogleLogin.as_view(),
        name='google_login'
    ),

    url(
        regex=r'^api/user-list-create/$',
        view=views.UserListCreate.as_view(),
        name='user-list-create'
    ),

    url(
        regex=r'^api/user-get-update/$',
        view=views.UserGetUpdate.as_view(),
        name='user-get-update'
    ),
]
