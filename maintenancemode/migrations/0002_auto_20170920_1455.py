# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-20 12:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenancemode', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='site',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
    ]