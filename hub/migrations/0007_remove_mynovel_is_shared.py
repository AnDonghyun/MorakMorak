# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 07:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0006_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mynovel',
            name='is_shared',
        ),
    ]