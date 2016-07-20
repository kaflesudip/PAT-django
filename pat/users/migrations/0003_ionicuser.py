# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160715_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='IonicUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ionic_id', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('sex', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=255)),
                ('zip_code', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('tos_accepted', models.BooleanField(default=False)),
                ('tos_accepted_datetime', models.DateField(null=True)),
            ],
        ),
    ]