# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_card_last_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='last_review',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
