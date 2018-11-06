# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 下午2:56
# @Author  : sing
from __future__ import unicode_literals
from django.views.generic import View
from django.shortcuts import render


class IndexView(View):
    def get(self, request):
        return render(request, 'base.html')
