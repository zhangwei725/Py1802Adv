# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-13 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=110, max_length=11),
            preserve_default=False,
        ),
    ]