# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-21 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.IntegerField(choices=[(0, '\u81ea\u5bfc\u4e70\u624b\u53f7'), (1, '\u7cfb\u7edf\u4e70\u624b\u53f7 -- 50\u79ef\u5206/\u6b21')], default='0', verbose_name='\u8d26\u53f7\u7c7b\u578b')),
                ('asin', models.CharField(max_length=250, verbose_name='Asin')),
                ('keyword', models.CharField(max_length=250, null=True, verbose_name='\u5173\u952e\u8bcd')),
                ('sellerid', models.CharField(max_length=250, null=True, verbose_name='SellerId')),
                ('brand', models.CharField(max_length=250, null=True, verbose_name='Brand')),
                ('total', models.IntegerField(default=0, verbose_name='\u52a0\u8d2d\u6b21\u6570')),
                ('wish', models.IntegerField(choices=[(0, '\u5426'), (1, '\u662f')], default='0', verbose_name='\u662f\u5426\u52a0WISH')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('starttime', models.DateTimeField(null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('sync_flag', models.BooleanField(default=0, verbose_name='\u4efb\u52a1\u5206\u914d')),
                ('finish', models.BooleanField(default=0, verbose_name='\u4efb\u52a1\u5b8c\u6210')),
                ('createuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_create_user', to='users.Userprofile', verbose_name='\u521b\u5efa\u4eba')),
                ('tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_tag', to='tags.Tag', verbose_name='\u6807\u7b7e')),
                ('updateuser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_update_user', to='users.Userprofile', verbose_name='\u66f4\u65b0\u4eba')),
            ],
            options={
                'db_table': 'cart',
                'verbose_name': '\u52a0\u8d2d',
                'verbose_name_plural': '\u52a0\u8d2d',
            },
        ),
    ]