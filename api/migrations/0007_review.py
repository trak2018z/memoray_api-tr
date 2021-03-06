# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 15:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20171008_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.Card')),
            ],
        ),
    ]
