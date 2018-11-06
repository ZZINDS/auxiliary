# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 下午2:09
# @Author  : sing

# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
import xadmin
from xadmin.views import BaseAdminPlugin, ListAdminView
from xadmin.plugins.utils import get_context_dict


class AddPlugin(BaseAdminPlugin):
    add_data = ''

    def init_request(self, *args, **kwargs):
        return self.add_data

    def block_top_toolbar(self, context, nodes):
        context.update({'forms': self.add_data})
        if self.add_data:
            nodes.append(
                loader.render_to_string('xadmin/extensions/model_list.top_toolbar.add_data.html',
                                        context=get_context_dict(context))
            )
