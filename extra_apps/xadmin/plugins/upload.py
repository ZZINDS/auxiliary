# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 下午2:58
# @Author  : sing

from django.template import loader
from xadmin.views import BaseAdminPlugin
from xadmin.plugins.utils import get_context_dict


class UploadPlugin(BaseAdminPlugin):
    upload = ''

    def init_request(self, *args, **kwargs):
        return self.upload

    def block_top_toolbar(self, context, nodes):
        context.update({'tags': self.upload})
        if self.upload:
            nodes.append(
                loader.render_to_string('xadmin/extensions/model_list.top_toolbar.upload.html',
                                        context=get_context_dict(context))
            )
