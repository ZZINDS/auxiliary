# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/9 9:22
@Author  : ZZINDS
@Site    : 
@File    : forms.py
@Software: PyCharm
"""
from django.forms import ModelForm
from django import forms
from models import Cart


class CartForm(ModelForm):
    account_CHOICES = (
        (0, u'自己的买手号'),
        (1, u'系统的买手号'),
    )
    starttime1 = forms.DateTimeField(widget=forms.DateInput(attrs={"class": "form-datetime am-form-field", "placeholder": u"填写中国时间"}), label="开始时间")

    class Meta:
        model = Cart
        exclude = ['id', 'createuser', 'starttime', 'createtime', 'updateuser', 'updatetime', 'delflag', "finish",  "sync_flag"]