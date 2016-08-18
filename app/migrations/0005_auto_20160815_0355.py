# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 03:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_auto_20160814_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('text', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('for_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='app.Question')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
                'ordering': ('-modified', '-created'),
            },
        ),
        migrations.CreateModel(
            name='Commentable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment_answer',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='comment_answer',
            name='for_item',
        ),
        migrations.RemoveField(
            model_name='comment_available',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='comment_available',
            name='for_item',
        ),
        migrations.RemoveField(
            model_name='comment_question',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='comment_question',
            name='for_item',
        ),
        migrations.RemoveField(
            model_name='comment_story',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='comment_story',
            name='for_item',
        ),
        migrations.RemoveField(
            model_name='comment_wanted',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='comment_wanted',
            name='for_item',
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='events'),
        ),
        migrations.DeleteModel(
            name='Comment_Answer',
        ),
        migrations.DeleteModel(
            name='Comment_Available',
        ),
        migrations.DeleteModel(
            name='Comment_Question',
        ),
        migrations.DeleteModel(
            name='Comment_Story',
        ),
        migrations.DeleteModel(
            name='Comment_Wanted',
        ),
    ]