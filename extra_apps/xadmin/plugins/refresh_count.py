# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
import xadmin
from xadmin.views import BaseAdminPlugin, ListAdminView
from xadmin.plugins.utils import get_context_dict


class RefreshCountPlugin(BaseAdminPlugin):
    refresh_count = False

    def init_request(self, *args, **kwargs):
        return self.refresh_count

    def block_top_toolbar(self, context, nodes):
        if self.refresh_count:
            nodes.append(
                loader.render_to_string('xadmin/extensions/model_list.top_toolbar.refresh_count.html',
                                        context=get_context_dict(context))
            )


# xadmin.site.register_plugin(RefreshCountPlugin, ListAdminView)
