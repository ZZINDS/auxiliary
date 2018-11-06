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
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(choices=[('A', 'ASIN'), ('S', 'SELLERID')], default='A', max_length=2, verbose_name='\u7c7b\u578b')),
                ('option', models.IntegerField(choices=[(0, '\u81ea\u5bfc\u4e70\u624b\u53f7'), (1, '\u7cfb\u7edf\u4e70\u624b\u53f7 -- 100\u79ef\u5206/\u6b21')], default='0', verbose_name='\u8d26\u53f7\u7c7b\u578b')),
                ('keyword', models.CharField(max_length=250, verbose_name='Asin')),
                ('total', models.IntegerField(default=0, verbose_name='\u8bc4\u8bba\u603b\u6570')),
                ('comment', models.TextField(verbose_name='\u8bc4\u8bba')),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('starttime', models.DateTimeField(null=True)),
                ('delflag', models.IntegerField(default=0)),
                ('finish', models.IntegerField(default=0)),
                ('review_flag', models.IntegerField(default=0)),
                ('start', models.IntegerField(default=5)),
                ('end', models.IntegerField(default=10)),
                ('name_type', models.IntegerField(choices=[(0, '\u9ed8\u8ba4\u59d3\u540d'), (1, '\u7537\u540d'), (2, '\u5973\u540d'), (3, '\u533f\u540d')], default='0', verbose_name='\u7559\u8bc4\u59d3\u540d')),
                ('sync_flag', models.IntegerField(default=0)),
                ('sync_review', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'review',
                'verbose_name': '\u7559\u8bc4',
                'verbose_name_plural': '\u7559\u8bc4',
            },
        ),
    ]