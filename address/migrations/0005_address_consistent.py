# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0004_finalise_version_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='consistent',
            field=models.BooleanField(default=False),
        ),
    ]
