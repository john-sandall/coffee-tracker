# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 13:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20160322_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brew',
            name='brew_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 22, 13, 58, 0, 199892, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='brew',
            name='date_ground',
            field=models.DateField(default=datetime.datetime(2016, 3, 22, 13, 58, 0, 200456, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='brew',
            name='date_roasted',
            field=models.DateField(default=datetime.datetime(2016, 3, 22, 13, 58, 0, 200411, tzinfo=utc)),
        ),
    ]
