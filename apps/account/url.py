# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 下午5:01
# @Author  : sing

from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^account/insert/', AccountInsertView.as_view()),
    url(r'^others/insert/', OthersInsertView.as_view()),
    url(r'^account/upload/', AccountUploadView.as_view()),
    url(r'^others/upload/', OthersUploadView.as_view()),
    url(r'^getlist', GetListView.as_view())
]
