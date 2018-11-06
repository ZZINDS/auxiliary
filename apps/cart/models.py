# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
from users.models import Userprofile
from tags.models import Tag
from account.models import Account


class Cart(models.Model):
    ACCOUNT_CHOICES = (
        (0, u'自导买手号'),
        (1, u'系统买手号 -- 50积分/次'),
    )

    WISH_CHOICES = (
        (0, u'否'),
        (1, u'是'),
    )
    tag = models.ForeignKey(Tag, related_name="cart_tag", null=True, verbose_name="标签")
    option = models.IntegerField(choices=ACCOUNT_CHOICES, default="0", verbose_name="账号类型")
    asin = models.CharField(max_length=250, null=False, verbose_name="Asin")
    keyword = models.CharField(max_length=250, null=True, verbose_name="关键词")
    sellerid = models.CharField(max_length=250, null=True, verbose_name="SellerId")
    brand = models.CharField(max_length=250, null=True, verbose_name="Brand")
    total = models.IntegerField(default=0, verbose_name="加购次数")
    wish = models.IntegerField(choices=WISH_CHOICES, default="0", verbose_name="是否加WISH")
    createuser = models.ForeignKey(verbose_name='创建人', to=Userprofile, related_name='cart_create_user',db_index=True)
    createtime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updatetime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    updateuser = models.ForeignKey(verbose_name='更新人', to=Userprofile, related_name='cart_update_user', null=True)
    starttime = models.DateTimeField(null=True, verbose_name="开始时间")
    sync_flag = models.BooleanField(verbose_name='任务分配', default=0)
    finish = models.BooleanField(verbose_name='任务完成', default=0)

    def __unicode__(self):
        return self.asin

    class Meta:
        verbose_name = '加购'
        verbose_name_plural = verbose_name
        db_table = "cart"


class Cart_allocation(models.Model):
    ACCOUNT_CHOICES = (
        (0, u'自导买手号'),
        (1, u'系统买手号 -- 50积分/次'),
    )
    WISH_CHOICES = (
        (0, u'否'),
        (1, u'是'),
    )
    cart = models.ForeignKey(verbose_name='加购', to = Cart)
    tag = models.ForeignKey(Tag, related_name="Cart_allocation_tag", null=True, verbose_name="平台")
    asin = models.CharField(max_length=250, null=False, verbose_name="ASIN")
    title = models.CharField(verbose_name='标题', max_length=200)
    option = models.IntegerField(choices=ACCOUNT_CHOICES, default="0", verbose_name="账号类型")
    keyword = models.CharField(max_length=250, null=True, verbose_name="关键词")
    sellerid = models.CharField(max_length=250, null=True, verbose_name="SellerId")
    brand = models.CharField(max_length=250, null=True, verbose_name="Brand")
    account = models.ForeignKey(verbose_name='加购账号', to=Account, related_name="Cart_allocation_account", null=True)
    total = models.IntegerField(default=0, verbose_name="加购次数")
    createuser = models.ForeignKey(verbose_name='创建人', to=Userprofile, related_name="Cart_allocation_by", db_index=True)
    createtime = models.DateTimeField(verbose_name='分配时间', auto_now_add=True)
    starttime = models.DateTimeField(verbose_name='开始时间', null=True, blank=True)
    carttime = models.DateTimeField(verbose_name='加购时间', null=True, blank=True)
    reviewid = models.CharField(verbose_name='加购ID', max_length=50, null=True)
    status = models.BooleanField(verbose_name='已加购', default=0)

    def __str__(self):
        return self.asin

    class Meta:
        db_table = "cart_allocation"
        verbose_name = '任务分配'
        verbose_name_plural = verbose_name