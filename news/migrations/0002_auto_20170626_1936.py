# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-26 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.CharField(max_length=255),
        ),
    ]