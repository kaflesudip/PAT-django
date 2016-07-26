# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        regex=r'^type-list/$',
        view=views.ActivityTypeList.as_view(),
        name='type_list'
    ),

    url(
        regex=r'^list-create/$',
        view=views.ActivityListCreate.as_view(),
        name='list_create'
    ),
]
