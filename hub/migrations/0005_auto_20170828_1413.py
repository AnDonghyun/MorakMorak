# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0004_mynovel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mynovel',
            name='status',
            field=models.CharField(choices=[('d', '작성중'), ('f', '작성완료'), ('p', '출판')], max_length=1),
        ),
    ]