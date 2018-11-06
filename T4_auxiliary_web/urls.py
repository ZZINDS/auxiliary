"""T4_auxiliary_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from tags import url as tag_url
from account import url as account_url
from review import url as review_url
from seckill import url as seckill_url
from cart import url as cart_url
from views import *
import xadmin
from xadmin.views.delete import DeleteView
from xadmin.views.website import RegisterView
from django.views.static import serve
from T4_auxiliary_web.settings import MEDIA_ROOT

urlpatterns = [
    url(r'delete/', DeleteView.as_view()),
    url(r'^', xadmin.site.urls),
    url(r'tags/tag/', include(tag_url)),
    url(r'account/', include(account_url)),
    url(r'review/', include(review_url)),
    url(r'seckill/seckill/', include(seckill_url)),
    url(r'cart/cart/', include(cart_url)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^register', RegisterView.as_view())
    # url(r'', IndexView.as_view()),
]
