# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 下午5:46
# @Author  : sing

from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^task/insert/', InsertView.as_view()),
    url(r'^queue/allocate/', AllocateView.as_view()),
    url(r'^queue/getlist/', GetListView.as_view()),
    url(r'^queue/post/', PostView.as_view())
]
