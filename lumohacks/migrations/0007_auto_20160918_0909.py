# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 09:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lumohacks', '0006_auto_20160918_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='name',
        ),
    ]
