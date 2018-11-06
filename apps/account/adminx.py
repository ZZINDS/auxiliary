# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 下午2:46
# @Author  : sing

import xadmin
from .models import Account, Others

from .forms import AccountForm, OthersForm
from tags.models import Tag


class AccountAdmin(object):
    add_data = AccountForm()
    del_data = True
    model_ordering = 2
    download = True
    upload = Tag.objects.all()
    model_icon = 'fa fa-user-o'
    # model_icon = 'glyphicon glyphicon-asterisk'
    list_display = ['name', 'email', 'password', 'enable_review', 'review_flag', 'tag']
    search_fields = ['name', 'email', 'password', 'enable_review', 'review_flag', 'tag']
    list_filter = ['name', 'email', 'password', 'enable_review', 'review_flag', 'tag']
    list_editable = ['enable_cookie']


class OthersAdmin(object):
    add_data = OthersForm()
    del_data = True
    model_ordering = 2
    download = True
    upload = Tag.objects.all()
    model_icon = 'fa fa-user-o'
    # model_icon = 'glyphicon glyphicon-asterisk'
    list_display = ['name', 'email', 'tag', 'proxy', 'browser', 'status']
    search_fields = ['name', 'email', 'tag', 'proxy', 'browser', 'status']
    list_filter = ['name', 'email', 'tag', 'proxy', 'browser', 'status']
    exclude = ['createuser']

    # def save_models(self):
    #     obj = self.new_obj
    #     obj.updateuser=self.user
    #     obj.save()
    #     self.delete_tags()
    # list_editable = ['enable_cookie']


xadmin.site.register(Account, AccountAdmin)
xadmin.site.register(Others, OthersAdmin)
