# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-14 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('review', '0015_auto_20180814_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='queue_tag', to='tags.Tag', verbose_name='\u5e73\u53f0'),
        ),
    ]
