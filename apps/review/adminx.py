# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 下午5:35
# @Author  : sing
from .models import Task, Queue
from .forms import TaskForm
import xadmin


class TaskAdmin(object):
    model_icon = 'fa fa-commenting-o'
    list_display = ['asin', 'comment', 'mode', 'option', 'createtime', 'starttime', 'sync_flag', 'finish']
    search_fields = ['asin', 'comment', 'mode', 'option', 'createtime', 'starttime', 'sync_flag', 'finish']
    list_filter = ['asin', 'comment', 'mode', 'option', 'createtime', 'starttime', 'sync_flag', 'finish']
    list_editable = ['sync_flag', 'finish']
    forms = TaskForm()
    add_data = forms
    del_data = True
    model_ordering = 3


class QueueAdmin(object):
    model_icon = 'fa fa-commenting-o'
    list_display = ['asin', 'title', 'content', 'account', 'createtime', 'starttime', 'reviewtime', 'reviewid',
                    'status']
    search_fields = ['asin', 'title', 'content', 'account', 'createtime', 'starttime', 'reviewtime', 'reviewid',
                     'status']
    list_filter = ['asin', 'title', 'content', 'account', 'createtime', 'starttime', 'reviewtime', 'reviewid', 'status']

    del_data = True


xadmin.site.register(Task, TaskAdmin)
xadmin.site.register(Queue, QueueAdmin)
