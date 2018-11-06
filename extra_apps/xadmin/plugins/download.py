# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
import xadmin
from xadmin.views import BaseAdminPlugin, ListAdminView
from xadmin.plugins.utils import get_context_dict


class DownloadPlugin(BaseAdminPlugin):
    download = False

    def init_request(self, *args, **kwargs):
        return self.download

    def block_top_toolbar(self, context, nodes):
        if self.download:
            nodes.append(
                loader.render_to_string('xadmin/extensions/model_list.top_toolbar.download.html',
                                        context=get_context_dict(context))
            )


# xadmin.site.register_plugin(DownloadPlugin, ListAdminView)
