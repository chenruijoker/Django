# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-01 07:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_auto_20190301_1550'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='students',
            options={'ordering': ['id']},
        ),
    ]
