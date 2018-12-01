# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-11-18 10:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip',
            name='inner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='innerIpAddress', to='resources.Server', verbose_name='内网IP'),
        ),
        migrations.AlterField(
            model_name='ip',
            name='public',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publicIpAddress', to='resources.Server', verbose_name='外网IP'),
        ),
    ]