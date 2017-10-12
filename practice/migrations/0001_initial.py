# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-03 01:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MomoReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='모모언니가 되어 사연에 답장해보세요!')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RadioStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=20, verbose_name='보내는 이')),
                ('content', models.TextField(help_text='모모언니에게 사연을 보내보세요!')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RelayNovelSequel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(help_text='이어지는 내용을 짧게 요약해 주세요!')),
                ('content', models.TextField(help_text='재치있게 소설을 이어나가 보세요!')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StartRelayNovel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='소설 제목')),
                ('content', models.TextField(help_text='새로운 릴레이 소설의 문을 열어보세요!')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='relaynovelsequel',
            name='StartRelayNovel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice.StartRelayNovel'),
        ),
        migrations.AddField(
            model_name='momoreply',
            name='RadioStation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice.RadioStation'),
        ),
    ]