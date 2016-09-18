# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 01:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lumohacks', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('note', models.TextField()),
                ('treatment', models.CharField(max_length=128)),
                ('duration', models.DecimalField(decimal_places=1, max_digits=5)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lumohacks.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lumohacks.Patient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]