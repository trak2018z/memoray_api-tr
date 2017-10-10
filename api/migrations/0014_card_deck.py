# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 09:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_deck'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='deck',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Deck'),
            preserve_default=False,
        ),
    ]
