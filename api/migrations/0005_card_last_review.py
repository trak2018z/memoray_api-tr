# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20171008_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='last_review',
            field=models.DateTimeField(default=None),
        ),
    ]
