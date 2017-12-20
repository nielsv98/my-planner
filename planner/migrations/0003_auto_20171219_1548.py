# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-19 14:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_auto_20171219_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2017, 12, 19, 14, 48, 47, 919914, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='starting_time',
            field=models.TimeField(default=datetime.datetime(2017, 12, 19, 14, 48, 47, 919914, tzinfo=utc)),
        ),
    ]