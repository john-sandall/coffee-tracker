# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 13:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20160322_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brew',
            name='brew_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='brew',
            name='date_ground',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='brew',
            name='date_roasted',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
