# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-19 02:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_auto_20190301_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str', tinymce.models.HTMLField()),
            ],
        ),
        migrations.AlterModelManagers(
            name='students',
            managers=[
                ('stuObj', django.db.models.manager.Manager()),
            ],
        ),
    ]
