# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-27 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('tags', '0002_auto_20180827_0912'),
        ('account', '0004_auto_20180814_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Others',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='\u8d26\u53f7')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='\u90ae\u7bb1')),
                ('password', models.CharField(max_length=255, null=True, verbose_name='\u5bc6\u7801')),
                ('cookies', models.TextField(null=True, verbose_name='cookie')),
                ('proxy', models.CharField(blank=True, choices=[('ZZ', '\u4f4f\u5b85IP'), ('GD', '\u56fa\u5b9aIP')], max_length=200, null=True, verbose_name='\u4ee3\u7406')),
                ('browser', models.CharField(blank=True, max_length=200, null=True, verbose_name='\u6d4f\u89c8\u5668')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updatetime', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('createuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='others_create_user', to='users.Userprofile', verbose_name='\u521b\u5efa\u4eba')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='others_tag', to='tags.Tag', verbose_name='\u6807\u7b7e')),
                ('updateuser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='others_update_user', to='users.Userprofile', verbose_name='\u66f4\u65b0\u4eba')),
            ],
            options={
                'db_table': 'others',
                'verbose_name': '\u6c42\u4ed6',
                'verbose_name_plural': '\u6c42\u4ed6',
            },
        ),
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': '\u7559\u8bc4', 'verbose_name_plural': '\u7559\u8bc4'},
        ),
    ]