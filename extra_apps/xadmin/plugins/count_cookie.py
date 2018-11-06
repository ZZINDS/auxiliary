# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 上午9:14
# @Author  : sing

import xadmin
from xadmin.views import BaseAdminPlugin, ListAdminView
from django.template import loader
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


# excel 导入
class CountCookiePlugin(BaseAdminPlugin):
    count_cookie = False

    # 这个函数返回true or false。如果为true会加载插件。
    def init_request(self, *args, **kwargs):
        return bool(self.count_cookie)

    def block_top_toolbar(self, context, nodes):
        # 指定我们渲染使用的模板html
        nodes.append(loader.render_to_string('xadmin/extensions/model_list.top_toolbar.count_cookie.html',
                                             get_context_dict(context)))


