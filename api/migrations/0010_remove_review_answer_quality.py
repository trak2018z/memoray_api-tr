# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 15:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20171008_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='answer_quality',
        ),
    ]