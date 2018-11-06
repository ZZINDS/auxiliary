# coding=utf-8
from __future__ import absolute_import

from django.utils.translation import ugettext as _
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.views.decorators.cache import never_cache
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.http import HttpResponse

from .base import BaseAdminView, filter_hook
from .dashboard import Dashboard
from xadmin.forms import AdminAuthenticationForm
from xadmin.models import UserSettings
from xadmin.layout import FormHelper


class IndexView(Dashboard):
    title = _("Main Dashboard")
    icon = "fa fa-dashboard"

    def get_page_id(self):
        return 'home'


class UserSettingView(BaseAdminView):

    @never_cache
    def post(self, request):
        key = request.POST['key']
        val = request.POST['value']
        us, created = UserSettings.objects.get_or_create(
            user=self.user, key=key)
        us.value = val
        us.save()
        return HttpResponse('')


class LoginView(BaseAdminView):
    title = _("Please Login")
    login_form = None
    login_template = None

    @filter_hook
    def update_params(self, defaults):
        pass

    @never_cache
    def get(self, request, *args, **kwargs):
        context = self.get_context()
        helper = FormHelper()
        helper.form_tag = False
        helper.include_media = False
        context.update({
            'title': self.title,
            'helper': helper,
            'app_path': request.get_full_path(),
            REDIRECT_FIELD_NAME: request.get_full_path(),
        })
        defaults = {
            'extra_context': context,
            'current_app': self.admin_site.name,
            'authentication_form': self.login_form or AdminAuthenticationForm,
            'template_name': self.login_template or 'xadmin/views/login.html',
        }
        self.update_params(defaults)
        return login(request, **defaults)

    @never_cache
    def post(self, request, *args, **kwargs):
        return self.get(request)


class LogoutView(BaseAdminView):
    logout_template = None
    need_site_permission = False

    @filter_hook
    def update_params(self, defaults):
        pass

    @never_cache
    def get(self, request, *args, **kwargs):
        context = self.get_context()
        defaults = {
            'extra_context': context,
            'current_app': self.admin_site.name,
            'template_name': self.logout_template or 'xadmin/views/logged_out.html',
        }
        if self.logout_template is not None:
            defaults['template_name'] = self.logout_template

        self.update_params(defaults)
        return logout(request, **defaults)

    @never_cache
    def post(self, request, *args, **kwargs):
        return self.get(request)


from django.views.generic import View
from django.shortcuts import render
from users.models import Userprofile
from django.contrib.auth.hashers import make_password
import random
import string


class RegisterView(View):
    register_html = 'xadmin/views/register.html'
    base_template = 'xadmin/base.html'

    def get(self, request):
        context = {
            'base_template': self.base_template,
        }
        return render(request, self.register_html, context=context)

    def post(self, request):
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if Userprofile.objects.filter(username=username):
            return render(request, self.register_html,
                          {'username': username, 'errors': '用户名已存在！', 'base_template': self.base_template})
        if password1 != password2:
            return render(request, self.register_html,
                          {'username': username, 'errors': '两次输入的密码不一致！', 'base_template': self.base_template})
        user = Userprofile()
        user.username = username
        user.password = make_password(password1)
        user.key = ''.join(random.sample(string.ascii_letters + string.digits, 16))
        user.iv = ''.join(random.sample(string.ascii_letters + string.digits, 16))
        user.token = ''.join(random.sample(string.ascii_letters + string.digits, 24))
        user.is_active = True
        user.save()
        return render(request, 'xadmin/views/register_success.html', {'base_template': 'xadmin/base.html'})


class RegisterSucessView(View):
    def get(self, request):
        return render(request, 'xadmin/views/register_success.html', {'base_template': 'xadmin/base.html'})
