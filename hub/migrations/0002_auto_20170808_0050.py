# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 15:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mynovel',
            old_name='user',
            new_name='author',
        ),
    ]
