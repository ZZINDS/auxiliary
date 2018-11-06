# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/9 10:12
@Author  : ZZINDS
@Site    : 
@File    : url.py
@Software: PyCharm
"""
from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'insert/', InsertView.as_view()),

]