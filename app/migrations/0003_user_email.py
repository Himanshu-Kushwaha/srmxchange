# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160723_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='null', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]