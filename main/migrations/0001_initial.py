# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-05-09 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(default=b'company', max_length=500)),
                ('phone', models.PositiveIntegerField(default=1)),
                ('subject', models.CharField(max_length=500)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('photo', models.ImageField(upload_to=b'')),
                ('leader', models.BooleanField(default=False)),
            ],
        ),
    ]
