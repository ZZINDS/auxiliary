# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-13 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='\u7ad9\u70b9')),
                ('url', models.URLField(verbose_name='\u94fe\u63a5')),
            ],
            options={
                'db_table': 'tag',
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
    ]
