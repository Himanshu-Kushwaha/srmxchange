# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 15:21
from __future__ import unicode_literals

from django.db import migrations
import django_html_cleaner.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20160816_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=django_html_cleaner.models.SanitizedTextField(),
        ),
        migrations.AlterField(
            model_name='available',
            name='text',
            field=django_html_cleaner.models.SanitizedTextField(),
        ),
        migrations.AlterField(
            model_name='available',
            name='title',
            field=django_html_cleaner.models.SanitizedCharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comment_answer',
            name='text',
            field=django_html_cleaner.models.SanitizedTextField(verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='comment_available',
            name='text',
            field=django_html_cleaner.models.SanitizedTextField(verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='comment_event',
            name='text',
            field=django_html_cleaner.models.SanitizedTextField(verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='comment_question',
            name='text',
            field=django_html_cleaner.models.SanitizedTextField(verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='comment_story',
            name='text',
            field=django_html_cleaner.models.SanitizedTextField(verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='comment_wanted',
            name='text',
            field=django_html_cleaner.models.SanitizedTextField(verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='event',
            name='text',
            field=django_html_cleaner.models.SanitizedTextField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=django_html_cleaner.models.SanitizedCharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='text',
            field=django_html_cleaner.models.SanitizedTextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=django_html_cleaner.models.SanitizedCharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=django_html_cleaner.models.SanitizedTextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=django_html_cleaner.models.SanitizedCharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='story',
            name='text',
            field=django_html_cleaner.models.SanitizedTextField(),
        ),
        migrations.AlterField(
            model_name='story',
            name='title',
            field=django_html_cleaner.models.SanitizedCharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='display_name',
            field=django_html_cleaner.models.SanitizedCharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=django_html_cleaner.models.SanitizedCharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=django_html_cleaner.models.SanitizedCharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_text',
            field=django_html_cleaner.models.SanitizedTextField(blank=True, max_length=500, null=True, verbose_name='Describe yourself'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='register_no',
            field=django_html_cleaner.models.SanitizedCharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='wanted',
            name='text',
            field=django_html_cleaner.models.SanitizedTextField(),
        ),
        migrations.AlterField(
            model_name='wanted',
            name='title',
            field=django_html_cleaner.models.SanitizedCharField(max_length=100),
        ),
    ]
