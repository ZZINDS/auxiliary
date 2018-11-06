# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 上午11:51
# @Author  : sing


import xadmin
from .models import Tag
from .forms import TagForm


class TagAdmin(object):
    forms = TagForm()
    add_data = forms
    del_data = True
    # model_icon = 'glyphicon glyphicon-asterisk'
    model_icon = 'fa fa-bookmark-o'
    model_ordering = 1
    list_display = ['name', 'url', 'proxy', 'desc']
    search_fields = ['name', 'url', 'proxy', 'desc']
    list_filter = ['name', 'url', 'proxy', 'desc']


xadmin.site.register(Tag, TagAdmin)
