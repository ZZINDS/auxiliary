# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-29 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20180827_1451'),
        ('users', '0001_initial'),
        ('tags', '0003_auto_20180827_1451'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_allocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(max_length=250, verbose_name='ASIN')),
                ('title', models.CharField(max_length=200, verbose_name='\u6807\u9898')),
                ('option', models.IntegerField(choices=[(0, '\u81ea\u5bfc\u4e70\u624b\u53f7'), (1, '\u7cfb\u7edf\u4e70\u624b\u53f7 -- 50\u79ef\u5206/\u6b21')], default='0', verbose_name='\u8d26\u53f7\u7c7b\u578b')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('keyword', models.CharField(max_length=250, null=True, verbose_name='\u5173\u952e\u8bcd')),
                ('sellerid', models.CharField(max_length=250, null=True, verbose_name='SellerId')),
                ('brand', models.CharField(max_length=250, null=True, verbose_name='Brand')),
                ('total', models.IntegerField(default=0, verbose_name='\u52a0\u8d2d\u6b21\u6570')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u5206\u914d\u65f6\u95f4')),
                ('starttime', models.DateTimeField(blank=True, null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('carttime', models.DateTimeField(blank=True, null=True, verbose_name='\u52a0\u8d2d\u65f6\u95f4')),
                ('reviewid', models.CharField(max_length=50, null=True, verbose_name='\u52a0\u8d2dID')),
                ('status', models.BooleanField(default=0, verbose_name='\u5df2\u52a0\u8d2d')),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Cart_allocation_account', to='account.Account', verbose_name='\u52a0\u8d2d\u8d26\u53f7')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart', verbose_name='\u52a0\u8d2d')),
                ('createuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cart_allocation_by', to='users.Userprofile', verbose_name='\u521b\u5efa\u4eba')),
                ('tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Cart_allocation_tag', to='tags.Tag', verbose_name='\u5e73\u53f0')),
            ],
            options={
                'db_table': 'cart_allocation',
                'verbose_name': '\u4efb\u52a1\u5206\u914d',
                'verbose_name_plural': '\u4efb\u52a1\u5206\u914d',
            },
        ),
    ]
