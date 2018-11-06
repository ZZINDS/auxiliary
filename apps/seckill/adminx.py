# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 下午1:38
# @Author  : sing
import xadmin
from .models import Seckill
from .forms import SeckillForm


class SeckillAdmin(object):
    list_display = ['asin', 'tag', 'kill_percent', 'now_percent', 'hours', 'count', 'status', 'begin_time', 'end_time']
    search_fields = ['asin', 'tag', 'begin_time', 'end_time', 'count', 'status']
    list_filter = ['asin', 'tag', 'begin_time', 'end_time', 'count', 'status']
    fields = ['asin', 'tag', 'kill_percent', 'begin_time', 'end_time']
    readonly_fields = ['status']

    add_data = SeckillForm()
    del_data = True
    model_ordering = 4
    model_icon = 'fa fa-bolt'


xadmin.site.register(Seckill, SeckillAdmin)
