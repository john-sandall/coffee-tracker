# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20160322_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bean',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vendor', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('grind', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('date_roasted', models.DateField(default=django.utils.timezone.now)),
                ('date_ground', models.DateField(default=django.utils.timezone.now)),
                ('ground_by', models.CharField(max_length=200)),
                ('hints_of', models.CharField(max_length=200)),
                ('roast_type', models.CharField(max_length=200)),
                ('producer', models.CharField(max_length=200)),
                ('process', models.CharField(max_length=200)),
                ('origin', models.CharField(max_length=200)),
                ('varietal', models.CharField(max_length=200)),
                ('altitude', models.CharField(max_length=200)),
                ('farmer_question', models.TextField()),
                ('farmer_answer', models.TextField()),
                ('tasting_notes_flavour', models.CharField(max_length=200)),
                ('tasting_notes_sweetness', models.CharField(max_length=200)),
                ('tasting_notes_acidity', models.CharField(max_length=200)),
                ('tasting_notes_mouthfeel', models.CharField(max_length=200)),
                ('pact_reviewer_name', models.CharField(max_length=200)),
                ('pact_reviewer_says', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='brew',
            name='kettle_boiled',
        ),
        migrations.AddField(
            model_name='brew',
            name='bean',
            field=models.ForeignKey(default=1, to='tracker.Bean'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brew',
            name='hot_water_added',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='brew',
            name='milk_added',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='brew',
            name='repour_into_mug',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='brew',
            name='sugar_added',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
