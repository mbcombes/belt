# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-24 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trip_buddy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='guest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='joined_trips', to='trip_buddy.User'),
        ),
    ]