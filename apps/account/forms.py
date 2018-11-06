# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 下午4:56
# @Author  : sing
from django.forms import ModelForm
from django import forms
from .models import Account, Others


class AccountForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": u"名称", "required": "required"}),
                           error_messages={"required": u"名称不能为空",
                                           "invalid": u"输入一个有效的名称",
                                           "unique": u"该名称已存在"},
                           strip=True,
                           label=u"名称")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': u'邮箱'}),
                             label=u"邮箱")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": u"密码", "required": "required"}),
        strip=True,
        label=u"密码")
    cookies = forms.CharField(widget=forms.Textarea(attrs={"placeholder": u"Cookies"}),
                              strip=True, required=False,
                              label=u"Cookies")

    class Meta:
        model = Account
        fields = ['name', 'email', 'password', 'cookies', 'tag']


class OthersForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": u"名称", "required": "required"}),
                           error_messages={"required": u"名称不能为空",
                                           "invalid": u"输入一个有效的名称",
                                           "unique": u"该名称已存在"},
                           strip=True,
                           label=u"名称")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': u'邮箱'}),
                             label=u"邮箱")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": u"密码", "required": "required"}),
        strip=True,
        label=u"密码")
    cookies = forms.CharField(widget=forms.Textarea(attrs={"placeholder": u"Cookies"}),
                              strip=True, required=False,
                              label=u"Cookies")

    class Meta:
        model = Others
        fields = ['name', 'email', 'password', 'cookies', 'proxy', 'browser', 'tag']
