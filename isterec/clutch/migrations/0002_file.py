# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clutch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/clutch/%Y/%m/%d')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clutch.ClutchRecData')),
            ],
        ),
    ]