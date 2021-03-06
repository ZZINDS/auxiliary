# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tags.models import Tag
from users.models import Userprofile


# Create your models here.

class Account(models.Model):
    name = models.CharField(verbose_name='用户名', max_length=50, db_index=True, null=False)
    email = models.EmailField(verbose_name='邮箱', null=True)
    password = models.CharField(verbose_name='密码', max_length=255, null=True)
    cookies = models.TextField(verbose_name='cookie', null=True)
    tag = models.ForeignKey(verbose_name='标签', to=Tag, related_name="account_tag", db_index=True)
    enable_cookie = models.NullBooleanField(verbose_name='cookie是否可用', default=None)
    enable_review = models.IntegerField(verbose_name='评论状态', default=0)
    review_flag = models.BooleanField(verbose_name='是否已评论', default=0)
    createuser = models.ForeignKey(verbose_name='创建人', to=Userprofile, related_name='account_create_user',
                                   db_index=True)
    createtime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updateuser = models.ForeignKey(verbose_name='更新人', to=Userprofile, related_name='account_update_user', null=True)
    updatetime = models.DateTimeField(verbose_name='更新时间', auto_now=True, null=True)

    # delflag = models.IntegerField('删除标志', default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "account"
        verbose_name = '留评'
        verbose_name_plural = verbose_name


class Others(models.Model):
    PROXY_CHOICES = (
        ('ZZ', '住宅IP'),
        ('GD', '固定IP'),
    )
    BROWSER_CHOICES = (
        ('R', '随机'),
        ('Chrome/61.0.3163.100-win10', 'Chrome/61.0.3163.100-win10'),
        ('Chrome/61.0.3163.100-win7', 'Chrome/61.0.3163.100-win7'),
        ('Chrome/61.0.3163.100-mac10.12', 'Chrome/61.0.3163.100-mac10.12'),
        ('Chrome/61.0.3163.100-win8', 'Chrome/61.0.3163.100-win8'),
        ('Chrome/61.0.3163.100-mac10.11', 'Chrome/61.0.3163.100-mac10.11'),
        ('Chrome/61.0.3163.100-win7X64', 'Chrome/61.0.3163.100-win7X64'),
        ('Chrome/61.0.3163.100-win8.1', 'Chrome/61.0.3163.100-win8.1'),
        ('Chrome/62.0.3202.75', 'Chrome/62.0.3202.75'),
        ('Chrome/62.0.3202.62', 'Chrome/62.0.3202.62'),
        ('Chrome/60.0.3112.113', 'Chrome/60.0.3112.113'),
        ('Chrome/61.0.3163.100-mac10.10', 'Chrome/61.0.3163.100-mac10.10'),
        ('Chrome/61.0.3163.100', 'Chrome/61.0.3163.100'),
        ('Chrome/61.0.3163.100-mac10.12', 'Chrome/61.0.3163.100-mac10.12'),
        ('Chrome/62.0.3202.75-win7', 'Chrome/62.0.3202.75-win7'),
        ('Chrome/62.0.3202.62-win7', 'Chrome/62.0.3202.62-win7'),
        ('Chrome/62.0.3202.75-linux', 'Chrome/62.0.3202.75-linux'),
        ('Chrome/42.0.2311.90-mac10.12', 'Chrome/42.0.2311.90-mac10.12'),
        ('Chrome/60.0.3112.113-mac10.12', 'Chrome/60.0.3112.113-mac10.12'),
        ('Chrome/61.0.3163.79', 'Chrome/61.0.3163.79'),
        ('Chrome/60.0.3112.78', 'Chrome/60.0.3112.78'),
        ('firefox58', 'firefox58'),
        ('firefox46', 'firefox46'),
        ('1firefox', '1firefox'),
        ('firefox22', 'firefox22'),
        ('firefox25', 'firefox25'),
        ('firefox25-macos', 'firefox25-macos'),
        ('firefox5', 'firefox5'),
        ('firefox6', 'firefox6'),
        ('firefox7', 'firefox7'),
        ('firefox40', 'firefox40'),
        ('Chrome/62.0.3202.89', 'Chrome/62.0.3202.89'),
        ('Chrome/49.0.2623.112', 'Chrome/49.0.2623.112'),
        ('Chrome/41.0.2272.118', 'Chrome/41.0.2272.118'),
        ('Chrome/62.0.3202.94', 'Chrome/62.0.3202.94'),
        ('Chrome/51.0.2704.79', 'Chrome/51.0.2704.79'),
        ('Chrome/54.0.2840.99', 'Chrome/54.0.2840.99'),
        ('Chrome/54.0.2840.99-Win10', 'Chrome/54.0.2840.99-Win10'),
        ('Chrome/60.0.3112.113-Win7', 'Chrome/60.0.3112.113-Win7'),
        ('Chrome/60.0.3112.90-Win7', 'Chrome/60.0.3112.90-Win7'),
        ('Chrome/52.0.2743.116-', 'Chrome/52.0.2743.116-'),
        ('Chrome/62.0.3202.89-Win7', 'Chrome/62.0.3202.89-Win7'),
        ('Chrome/56.0.2924.87-Win7', 'Chrome/56.0.2924.87-Win7'),
        ('Chrome/52.0.2743.116-Win7', 'Chrome/52.0.2743.116-Win7'),
        ('Chrome/51.0.2704.106-Win7', 'Chrome/51.0.2704.106-Win7'),
        ('Chrome/42.0.2311.90-Win7', 'Chrome/42.0.2311.90-Win7'),
        ('Chrome/52.0.2743.82-Win10', 'Chrome/52.0.2743.82-Win10'),
        ('Chrome/61.0.3163.100-Win7', 'Chrome/61.0.3163.100-Win7'),
        ('Chrome/62.0.3202.89-', 'Chrome/62.0.3202.89-'),
        ('Chrome/54.0.2840.99-Win7', 'Chrome/54.0.2840.99-Win7'),
        ('Chrome/46.0.2490.80-', 'Chrome/46.0.2490.80-'),
        ('Chrome/51.0.2704.106-', 'Chrome/51.0.2704.106-'),
        ('Chrome/51.0.2704.63-', 'Chrome/51.0.2704.63-'),
        ('Chrome/61.0.3163.79-Win10', 'Chrome/61.0.3163.79-Win10'),
        ('Chrome/62.0.3202.62-', 'Chrome/62.0.3202.62-'),
        ('Chrome/55.0.2883.87-Win7', 'Chrome/55.0.2883.87-Win7'),
        ('Chrome/45.0.2454.101-', 'Chrome/45.0.2454.101-'),
        ('Chrome/53.0.2785.116-Win7', 'Chrome/53.0.2785.116-Win7'),
        ('Chrome/50.0.2661.94-', 'Chrome/50.0.2661.94-'),
        ('Chrome/49.0.2623.110-Win7', 'Chrome/49.0.2623.110-Win7'),
        ('Chrome/55.0.2883.87-', 'Chrome/55.0.2883.87-'),
        ('Chrome/56.0.2924.87-Win10', 'Chrome/56.0.2924.87-Win10'),
        ('Chrome/58.0.3029.110-Win7', 'Chrome/58.0.3029.110-Win7'),
        ('Chrome/57.0.2987.133-Win10', 'Chrome/57.0.2987.133-Win10'),
        ('Chrome/49.0.2623.110-Win10', 'Chrome/49.0.2623.110-Win10'),
        ('Chrome/47.0.2526.106-', 'Chrome/47.0.2526.106-'),
        ('Chrome/47.0.2526.106-Win10', 'Chrome/47.0.2526.106-Win10'),
        ('Chrome/62.0.3202.94-Win10', 'Chrome/62.0.3202.94-Win10'),
        ('Chrome/46.0.2490.80-Win7', 'Chrome/46.0.2490.80-Win7'),
        ('Chrome/45.0.2454.101-Win7', 'Chrome/45.0.2454.101-Win7'),
        ('Chrome/61.0.3163.100-Win10', 'Chrome/61.0.3163.100-Win10'),
        ('Chrome/48.0.2564.116-Win10', 'Chrome/48.0.2564.116-Win10'),
        ('Chrome/51.0.2704.103-Win7', 'Chrome/51.0.2704.103-Win7'),
        ('Chrome/51.0.2704.63-Win7', 'Chrome/51.0.2704.63-Win7'),
        ('Chrome/60.0.3112.113-Linux', 'Chrome/60.0.3112.113-Linux'),
        ('Chrome/48.0.2564.116-Win7', 'Chrome/48.0.2564.116-Win7'),
        ('Chrome/54.0.2840.59-Win7', 'Chrome/54.0.2840.59-Win7'),
        ('Chrome/61.0.3163.100-', 'Chrome/61.0.3163.100-'),
        ('Chrome/45.0.2454.85-Win7', 'Chrome/45.0.2454.85-Win7'),
        ('Chrome/60.0.3112.78-Win10', 'Chrome/60.0.3112.78-Win10'),
        ('Chrome/24.0.1312.57-Win7', 'Chrome/24.0.1312.57-Win7'),
        ('Chrome/58.0.3029.81-Win7', 'Chrome/58.0.3029.81-Win7'),
        ('Chrome/60.0.3112.101-Win7', 'Chrome/60.0.3112.101-Win7'),
        ('Chrome/43.0.2357.65-Win7', 'Chrome/43.0.2357.65-Win7'),
        ('Chrome/48.0.2564.97-Win7', 'Chrome/48.0.2564.97-Win7'),
        ('Chrome/60.0.3112.90-Win10', 'Chrome/60.0.3112.90-Win10'),
        ('Chrome/49.0.2623.112-', 'Chrome/49.0.2623.112-'),
        ('Chrome/57.0.2987.133-Win7', 'Chrome/57.0.2987.133-Win7'),
        ('Chrome/60.0.3112.78-Win7', 'Chrome/60.0.3112.78-Win7'),
        ('Chrome/25.0.1364.172-Win7', 'Chrome/25.0.1364.172-Win7'),
        ('Chrome/58.0.3029.81-Win10', 'Chrome/58.0.3029.81-Win10'),
        ('Chrome/60.0.3112.101-Win10', 'Chrome/60.0.3112.101-Win10'),
        ('Chrome/49.0.2623.112-Win7', 'Chrome/49.0.2623.112-Win7'),
        ('Chrome/60.0.3112.113-', 'Chrome/60.0.3112.113-'),
        ('Chrome/45.0.2454.93-Win10', 'Chrome/45.0.2454.93-Win10'),
        ('Chrome/49.0.2623.87-', 'Chrome/49.0.2623.87-'),
        ('Chrome/54.0.2840.99-', 'Chrome/54.0.2840.99-'),
        ('Chrome/58.0.3029.110-', 'Chrome/58.0.3029.110-'),
        ('Chrome/51.0.2704.106-Win10', 'Chrome/51.0.2704.106-Win10'),
        ('Chrome/43.0.2357.65-', 'Chrome/43.0.2357.65-'),
        ('Chrome/47.0.2526.106-Win7', 'Chrome/47.0.2526.106-Win7'),
        ('Chrome/49.0.2623.87-Win7', 'Chrome/49.0.2623.87-Win7'),
        ('Chrome/49.0.2623.112-Win10', 'Chrome/49.0.2623.112-Win10'),
        ('Chrome/59.0.3071.115-Win10', 'Chrome/59.0.3071.115-Win10'),
        ('Chrome/60.0.3112.90-', 'Chrome/60.0.3112.90-'),
        ('Chrome/26.0.1410.64-Win7', 'Chrome/26.0.1410.64-Win7'),
        ('Chrome/48.0.2564.109-', 'Chrome/48.0.2564.109-'),
        ('Chrome/53.0.2785.116-Win10', 'Chrome/53.0.2785.116-Win10'),
        ('Chrome/53.0.2785.143-Win7', 'Chrome/53.0.2785.143-Win7'),
        ('Chrome/51.0.2704.103-Win10', 'Chrome/51.0.2704.103-Win10'),
        ('Chrome/59.0.3071.86-Win10', 'Chrome/59.0.3071.86-Win10'),
        ('Chrome/41.0.2228.0-Win7', 'Chrome/41.0.2228.0-Win7'),
        ('Chrome/48.0.2564.109-Win10', 'Chrome/48.0.2564.109-Win10'),
        ('Chrome/54.0.2840.71-Win7', 'Chrome/54.0.2840.71-Win7'),
        ('Chrome/60.0.3112.78-Linux', 'Chrome/60.0.3112.78-Linux'),
        ('Chrome/51.0.2704.84-Win10', 'Chrome/51.0.2704.84-Win10'),
        ('Chrome/58.0.3029.96-Win10', 'Chrome/58.0.3029.96-Win10'),
        ('Chrome/54.0.2840.71-Win10', 'Chrome/54.0.2840.71-Win10'),
        ('Chrome/62.0.3202.75-Win10', 'Chrome/62.0.3202.75-Win10'),
        ('Chrome/53.0.2785.143-Win10', 'Chrome/53.0.2785.143-Win10'),
        ('Chrome/47.0.2526.111-Win7', 'Chrome/47.0.2526.111-Win7'),
        ('Chrome/52.0.2743.116-Win10', 'Chrome/52.0.2743.116-Win10'),
        ('Chrome/57.0.2987.133-', 'Chrome/57.0.2987.133-'),
        ('Chrome/60.0.3112.113-Win10', 'Chrome/60.0.3112.113-Win10'),
        ('Chrome/52.0.2743.82-Win7', 'Chrome/52.0.2743.82-Win7'),
        ('Chrome/50.0.2661.102-Win7', 'Chrome/50.0.2661.102-Win7'),
        ('Chrome/59.0.3071.115-Win7', 'Chrome/59.0.3071.115-Win7'),
        ('Chrome/58.0.3029.110-Win10', 'Chrome/58.0.3029.110-Win10'),
        ('Chrome/46.0.2490.86-', 'Chrome/46.0.2490.86-'),
        ('Chrome/46.0.2490.86-Win7', 'Chrome/46.0.2490.86-Win7'),
        ('Chrome/48.0.2564.109-Win7', 'Chrome/48.0.2564.109-Win7'),
        ('Chrome/59.0.3071.115-Linux', 'Chrome/59.0.3071.115-Linux'),
        ('Chrome/61.0.3163.100-Linux', 'Chrome/61.0.3163.100-Linux'),
        ('Chrome/41.0.2272.104-Win7', 'Chrome/41.0.2272.104-Win7'),
        ('Chrome/49.0.2623.87-Win10', 'Chrome/49.0.2623.87-Win10'),
        ('Chrome/47.0.2526.111-Win10', 'Chrome/47.0.2526.111-Win10'),
        ('Chrome/62.0.3202.75-', 'Chrome/62.0.3202.75-'),
        ('Chrome/50.0.2661.102-Win10', 'Chrome/50.0.2661.102-Win10'),
        ('Chrome/44.0.2403.157-Win7', 'Chrome/44.0.2403.157-Win7'),
        ('Chrome/51.0.2704.106-Linux', 'Chrome/51.0.2704.106-Linux'),
        ('Chrome/46.0.2490.86-Win10', 'Chrome/46.0.2490.86-Win10'),
        ('Chrome/62.0.3202.62-Win10', 'Chrome/62.0.3202.62-Win10'),
        ('Chrome/62.0.3202.62-Win7', 'Chrome/62.0.3202.62-Win7'),
        ('Chrome/39.0.2171.95-Win7', 'Chrome/39.0.2171.95-Win7'),
        ('Chrome/59.0.3071.109-', 'Chrome/59.0.3071.109-'),
        ('Chrome/47.0.2526.80-Win7', 'Chrome/47.0.2526.80-Win7'),
        ('Chrome/62.0.3202.62-Linux', 'Chrome/62.0.3202.62-Linux'),
        ('Chrome/48.0.2564.116-', 'Chrome/48.0.2564.116-'),
        ('Chrome/45.0.2454.101-Win10', 'Chrome/45.0.2454.101-Win10'),
        ('Chrome/55.0.0.12195-Win10', 'Chrome/55.0.0.12195-Win10'),
        ('Chrome/46.0.2490.80-Win10', 'Chrome/46.0.2490.80-Win10'),
        ('Chrome/55.0.2883.87-Win10', 'Chrome/55.0.2883.87-Win10'),
        ('Chrome/62.0.3202.75-Win7', 'Chrome/62.0.3202.75-Win7'),
        ('Chrome/56.0.2924.87-', 'Chrome/56.0.2924.87-'),
        ('Chrome/46.0.2490.71-Win7', 'Chrome/46.0.2490.71-Win7'),
        ('Chrome/50.0.2661.94-Win7', 'Chrome/50.0.2661.94-Win7'),
        ('Chrome/45.0.2454.93-Win7', 'Chrome/45.0.2454.93-Win7'),
        ('Chrome/51.0.2704.84-Win7', 'Chrome/51.0.2704.84-Win7'),
        ('Chrome/50.0.2661.94-Win10', 'Chrome/50.0.2661.94-Win10'),
        ('Chrome/51.0.2704.103-', 'Chrome/51.0.2704.103-'),
        ('Chrome/59.0.3071.115-', 'Chrome/59.0.3071.115-'),
        ('Chrome/62.0.3202.89-Linux', 'Chrome/62.0.3202.89-Linux'),
    )
    STATUS_CHOICES = (
        ('Y', '已注册'),
        ('N', '未注册'),
    )
    name = models.CharField(verbose_name='账号', max_length=50, db_index=True, null=False)
    email = models.EmailField(verbose_name='邮箱', null=True)
    password = models.CharField(verbose_name='密码', max_length=255, null=True)
    cookies = models.TextField(verbose_name='cookie', null=True)
    proxy = models.CharField(verbose_name='代理', choices=PROXY_CHOICES, max_length=200,
                             default='ZZ')
    # tag_proxy = models.CharField(verbose_name='代理',  max_length=200)

    browser = models.CharField(verbose_name='浏览器', max_length=200, choices=BROWSER_CHOICES,
                               default='R')
    tag = models.ForeignKey(verbose_name='标签', to=Tag, related_name="others_tag", db_index=True)

    status = models.CharField(verbose_name='注册状态', null=True, blank=True, max_length=20, choices=STATUS_CHOICES,
                              default='Y')
    createuser = models.ForeignKey(verbose_name='创建人', to=Userprofile, related_name='others_create_user',
                                   db_index=True)
    createtime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = "others"
        verbose_name = '账号'
        verbose_name_plural = verbose_name
