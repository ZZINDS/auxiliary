# -*- coding: utf-8 -*-
# @Time    : 2018/8/9 下午5:32
# @Author  : sing
from django.forms import ModelForm
from django import forms
from datetime import datetime
from .models import Seckill


class SeckillForm(ModelForm):
    starttime1 = forms.DateTimeField(
        widget=forms.DateInput(attrs={"class": "form-datetime am-form-field", "placeholder": datetime.now}),
        label="开始时间")

    starttime2 = forms.DateTimeField(
        widget=forms.DateInput(attrs={"class": "form-datetime am-form-field", "placeholder": datetime.now}),
        label="结束时间")

    class Meta:
        model = Seckill
        fields = ['asin', 'tag', 'kill_percent', 'starttime1', 'starttime2']
