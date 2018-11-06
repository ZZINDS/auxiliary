# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
import xadmin
from xadmin.views import BaseAdminPlugin, ListAdminView
from xadmin.plugins.utils import get_context_dict


class CartEndPlugin(BaseAdminPlugin):
    cart_end = False

    def init_request(self, *args, **kwargs):
        return self.cart_end

    def block_top_toolbar(self, context, nodes):
        if self.cart_end:
            nodes.append(
                loader.render_to_string('xadmin/extensions/model_list.top_toolbar.cart_end.html',
                                        context=get_context_dict(context))
            )

# xadmin.site.register_plugin(RefreshCountPlugin, ListAdminView)
