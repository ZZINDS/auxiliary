# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
import xadmin
from xadmin.views import BaseAdminPlugin, ListAdminView
from xadmin.plugins.utils import get_context_dict


class QueueNormalPlugin(BaseAdminPlugin):
    queue_normal = False

    def init_request(self, *args, **kwargs):
        return self.queue_normal

    def block_top_toolbar(self, context, nodes):
        if self.queue_normal:
            nodes.append(
                loader.render_to_string('xadmin/extensions/model_list.top_toolbar.queue_normal.html',
                                        context=get_context_dict(context))
            )

# xadmin.site.register_plugin(RefreshCountPlugin, ListAdminView)
