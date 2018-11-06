# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 下午5:01
# @Author  : sing

from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^insert/', InsertView.as_view()),
]
