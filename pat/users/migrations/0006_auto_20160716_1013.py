# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20160716_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ionicuser',
            name='ionic_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]