# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 13:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='profile',
            table='auth_profile',
        ),
    ]
