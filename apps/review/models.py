# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from tags.models import Tag
from users.models import Userprofile
from account.models import Account


class Task(models.Model):
    MODE_CHOICES = (
        (u'A', u'ASIN'),
        (u'S', u'SELLERID'),
    )
    ACCOUNT_CHOICES = (
        (0, u'自导买手号'),
        (1, u'系统买手号'),
    )
    Name_CHOICES = (
        (0, u'默认姓名'),
        (1, u'男名'),
        (2, u'女名'),
        (3, u'匿名'),
    )

    tag = models.ForeignKey(Tag, related_name="task_tag", null=True, verbose_name="平台")
    mode = models.CharField(max_length=2, choices=MODE_CHOICES, default="A", verbose_name="类型")
    option = models.IntegerField(choices=ACCOUNT_CHOICES, default="0", verbose_name="账号类型")
    asin = models.CharField(max_length=250, null=False, verbose_name="ASIN")
    # total = models.IntegerField(default=0, verbose_name="评论总数")
    comment = models.TextField(null=False, verbose_name="评论")
    createuser = models.ForeignKey(verbose_name='创建人', to=Userprofile, related_name="rank_create_user")
    createtime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updateuser = models.ForeignKey(verbose_name='更新人', to=Userprofile, null=True, related_name="rank_update_user")
    updatetime = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    starttime = models.DateTimeField(verbose_name='预约时间', null=True)
    # delflag = models.IntegerField(default=0)
    # finish = models.IntegerField(default=0)
    # review_flag = models.IntegerField(default=0)
    # start = models.IntegerField(verbose_name='评论间隔从', default=5)
    # end = models.IntegerField(verbose_name='评论间隔至', default=10)
    name_type = models.IntegerField(choices=Name_CHOICES, default="0", verbose_name="留评姓名")
    sync_flag = models.BooleanField(verbose_name='任务分配', default=0)
    finish = models.BooleanField(verbose_name='任务完成', default=0)

    def __str__(self):
        return self.asin

    class Meta:
        db_table = "task"
        verbose_name = '任务'
        verbose_name_plural = verbose_name


class Queue(models.Model):
    Name_CHOICES = (
        (0, u'默认姓名'),
        (1, u'男名'),
        (2, u'女名'),
        (3, u'匿名'),
    )
    task = models.ForeignKey(verbose_name='任务', to=Task)
    tag = models.ForeignKey(Tag, related_name="queue_tag", null=True, verbose_name="平台")
    asin = models.CharField(max_length=250, null=False, verbose_name= "ASIN")
    title = models.CharField(verbose_name='标题', max_length=200)
    content = models.TextField(verbose_name='内容')
    account = models.ForeignKey(verbose_name='评论账号', to=Account, related_name="queue_account", null=True)
    name_type = models.IntegerField(choices=Name_CHOICES, default="0", verbose_name="留评姓名")
    createuser = models.ForeignKey(verbose_name='创建人', to=Userprofile, related_name="queue_by", db_index=True)
    createtime = models.DateTimeField(verbose_name='分配时间', auto_now_add=True)
    starttime = models.DateTimeField(verbose_name='预约时间', null=True, blank=True)
    reviewtime = models.DateTimeField(verbose_name='评论时间', null=True, blank=True)
    reviewid = models.CharField(verbose_name='评论ID', max_length=50, null=True)
    status = models.BooleanField(verbose_name='已评论', default=0)

    def __str__(self):
        return self.asin

    class Meta:
        db_table = "queue"
        verbose_name = '队列'
        verbose_name_plural = verbose_name
