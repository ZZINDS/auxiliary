# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader

import xadmin
from xadmin.views import BaseAdminPlugin, ListAdminView

from django.template.context import RequestContext


def get_context_dict(context):
    """
     Contexts in django version 1.9+ must be dictionaries. As xadmin has a legacy with older versions of django,
    the function helps the transition by converting the [RequestContext] object to the dictionary when necessary.
    :param context: RequestContext
    :return: dict
    """
    if isinstance(context, RequestContext):
        ctx = context.flatten()
    else:
        ctx = context
    return ctx


class DemoPlugin(BaseAdminPlugin):
    demo_plugin = False

    def init_request(self, *args, **kwargs):
        return self.demo_plugin

    def block_top_toolbar(self, context, nodes):
        if self.demo_plugin:
            content = '元素列表'
            context.update({
                'about_content': content
            })

        nodes.append(
            loader.render_to_string('xadmin/demo/model_list.top_toolbar.demo.html', get_context_dict(context))
        )


# xadmin.site.register_plugin(DemoPlugin, ListAdminView)
