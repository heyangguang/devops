# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-30 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='idc',
            name='status',
            field=models.BooleanField(choices=[(0, 'enabled'), (1, 'disabled')], default=0),
        ),
    ]
