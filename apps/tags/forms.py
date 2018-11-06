# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 上午11:51
# @Author  : sing
from django.forms import ModelForm
from .models import Tag


class TagForm(ModelForm):
    class Meta:
        model = Tag
        exclude = ['id']
