# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/9 9:18
@Author  : ZZINDS
@Site    : 
@File    : adminx.py
@Software: PyCharm
"""
import xadmin
from .models import Cart, Cart_allocation

from forms import CartForm


class CartAdmin(object):
    forms = CartForm()
    add_data = forms
    del_data = True
    model_icon = 'fa fa-plus'
    list_display = ['tag', 'option',  'asin', 'total', 'keyword', 'option',  'createtime', 'starttime', 'sync_flag', 'finish', ]
    search_fields = ['asin', 'total', 'keyword', 'option', 'createtime', 'starttime', 'sync_flag', 'finish', ]
    list_filter = ['asin', 'total', 'keyword', 'option', 'createtime', 'starttime', 'sync_flag', 'finish', ]
    list_editable = ['sync_flag', 'finish']


class Cart_allocationAdmin(object):

    del_data = True
    model_icon = 'fa fa-plus'
    list_display = ['tag', 'option',  'asin', 'total', 'keyword', 'option',  'createtime', 'starttime', 'status', ]
    search_fields = ['asin', 'total', 'keyword', 'option', 'createtime', 'starttime', 'status', ]
    list_filter = ['asin', 'total', 'keyword', 'option', 'createtime', 'starttime', 'status', ]


xadmin.site.register(Cart, CartAdmin)
xadmin.site.register(Cart_allocation, Cart_allocationAdmin)
# xadmin.site.register(views.BaseAdminView, BaseSetting)
# xadmin.site.register(views.CommAdminView, GlobalSettings)