# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 22:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_auto_20161219_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialCredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=50)),
                ('password', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=30)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]