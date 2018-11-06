# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 下午5:43
# @Author  : sing
from django.forms import ModelForm
from django import forms
from .models import Task
from datetime import datetime
from django.core.exceptions import ValidationError


# def comment_validate(comment):
#     comments = comment.strip().strip('\r\n').split('\r\n')
#     for com in comments:
#         coms = com.split('|')
#     raise ValidationError('邮箱格式错误')


class TaskForm(ModelForm):
    MODE_CHOICES = (
        (u'A', u'ASIN'),
        (u'S', u'SELLERID'),
    )
    starttime1 = forms.DateTimeField(
        widget=forms.DateInput(attrs={"class": "form-datetime am-form-field", "placeholder": datetime.now}), label="开始时间")
    comment = forms.CharField(
        # validators=[comment_validate, ],
                              widget=forms.Textarea(
                                  attrs={"placeholder": u"评论以 | 符号分割, | 前面为评论的HeadLine,后面的为内容,一条评论一行.注: | 符号必须为英文符号"}),
                              label=u"评论")
    # time_begin = forms.CharField(widget=forms.NumberInput(attrs={"value": 5}), label='评论间隔从')
    # time_end = forms.CharField(widget=forms.NumberInput(attrs={"value": 10}), label='评论间隔至')

    class Meta:
        model = Task
        exclude = ['id', 'createuser', 'createtime', 'updateuser', 'updatetime', 'delflag', "finish", "review_flag",
                   "sync_flag", "sync_review", "start", "end", 'starttime']
