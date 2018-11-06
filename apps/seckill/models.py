# coding=utf-8
from django.db import models

# Create your models here.
from datetime import datetime
from tags.models import Tag
from django.utils.safestring import mark_safe

class Seckill(models.Model):
    asin = models.CharField(verbose_name='ASIN', max_length=100)
    tag = models.ForeignKey(to=Tag, verbose_name='标签', max_length=100, )
    kill_percent = models.IntegerField(verbose_name='秒杀百分比', default=0)
    now_percent = models.IntegerField(verbose_name='当前百分比', default=0)
    begin_time = models.DateTimeField(verbose_name='开始时间', default=datetime.now, blank=True)
    end_time = models.DateTimeField(verbose_name='结束时间', default=datetime.now, blank=True)
    hours = models.CharField(verbose_name='剩余时间', max_length=100, blank=True, null=True)
    count = models.IntegerField(verbose_name='已加购次数', default=0)
    options = (
        ('begin', '未开始'),
        ('process', '运行中'),
        ('stop', '已停止'),
        ('end', '已结束')
    )
    status = models.CharField(verbose_name='状态', choices=options, max_length=10, default='begin')
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    def __str__(self):
        return self.asin

    class Meta:
        verbose_name = '秒杀'
        verbose_name_plural = verbose_name
        db_table = 'seckill'
