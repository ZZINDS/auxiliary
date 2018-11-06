# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Userprofile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='', null=True, blank=True)
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(max_length=7, verbose_name='性别', choices=(('male', '男'), ('female', '女')),
                              default='female')
    key = models.CharField(max_length=30, null=True, blank=True, default='adminBd4E2o7Zbhx')
    iv = models.CharField(max_length=30, null=True, blank=True, default='adminUTXkGNbwr5t')
    token = models.CharField(max_length=50, null=True, blank=True, default='admin0mRAcvCp85ZfhiX2jka')
    address = models.CharField(max_length=100, verbose_name='地址', default='', null=True, blank=True)
    mobile = models.CharField(max_length=11, verbose_name='手机号码', null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m', verbose_name='图片', default='image/default.png', max_length=100,
                              null=True, blank=True)

    class Meta:
        db_table = 'userprofile'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
