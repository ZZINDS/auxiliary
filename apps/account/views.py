# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import csv
import json
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from .models import Account
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from Crypto.Cipher import AES
import base64
from django.db import connection, transaction, IntegrityError
from users.models import Userprofile
import time
from datetime import datetime
from tags.models import Tag
import random

browser_list = [
    'Chrome/61.0.3163.100-win10',
    'Chrome/61.0.3163.100-win7',
    'Chrome/61.0.3163.100-mac10.12',
    'Chrome/61.0.3163.100-win8',
    'Chrome/61.0.3163.100-mac10.11',
    'Chrome/61.0.3163.100-win7X64',
    'Chrome/61.0.3163.100-win8.1',
    'Chrome/62.0.3202.75',
    'Chrome/62.0.3202.62',
    'Chrome/60.0.3112.113',
    'Chrome/61.0.3163.100-mac10.10',
    'Chrome/61.0.3163.100',
    'Chrome/61.0.3163.100-mac10.12',
    'Chrome/62.0.3202.75-win7',
    'Chrome/62.0.3202.62-win7',
    'Chrome/62.0.3202.75-linux',
    'Chrome/42.0.2311.90-mac10.12',
    'Chrome/60.0.3112.113-mac10.12',
    'Chrome/61.0.3163.79',
    'Chrome/60.0.3112.78',
    'firefox58',
    'firefox46',
    '1firefox',
    'firefox22',
    'firefox25',
    'firefox25-macos',
    'firefox5',
    'firefox6',
    'firefox7',
    'firefox40',
    'Chrome/62.0.3202.89',
    'Chrome/49.0.2623.112',
    'Chrome/41.0.2272.118',
    'Chrome/62.0.3202.94',
    'Chrome/51.0.2704.79',
    'Chrome/54.0.2840.99',
    'Chrome/54.0.2840.99-Win10',
    'Chrome/60.0.3112.113-Win7',
    'Chrome/60.0.3112.90-Win7',
    'Chrome/52.0.2743.116-',
    'Chrome/62.0.3202.89-Win7',
    'Chrome/56.0.2924.87-Win7',
    'Chrome/52.0.2743.116-Win7',
    'Chrome/51.0.2704.106-Win7',
    'Chrome/42.0.2311.90-Win7',
    'Chrome/52.0.2743.82-Win10',
    'Chrome/61.0.3163.100-Win7',
    'Chrome/62.0.3202.89-',
    'Chrome/54.0.2840.99-Win7',
    'Chrome/46.0.2490.80-',
    'Chrome/51.0.2704.106-',
    'Chrome/51.0.2704.63-',
    'Chrome/61.0.3163.79-Win10',
    'Chrome/62.0.3202.62-',
    'Chrome/55.0.2883.87-Win7',
    'Chrome/45.0.2454.101-',
    'Chrome/53.0.2785.116-Win7',
    'Chrome/50.0.2661.94-',
    'Chrome/49.0.2623.110-Win7',
    'Chrome/55.0.2883.87-',
    'Chrome/56.0.2924.87-Win10',
    'Chrome/58.0.3029.110-Win7',
    'Chrome/57.0.2987.133-Win10',
    'Chrome/49.0.2623.110-Win10',
    'Chrome/47.0.2526.106-',
    'Chrome/47.0.2526.106-Win10',
    'Chrome/62.0.3202.94-Win10',
    'Chrome/46.0.2490.80-Win7',
    'Chrome/45.0.2454.101-Win7',
    'Chrome/61.0.3163.100-Win10',
    'Chrome/48.0.2564.116-Win10',
    'Chrome/51.0.2704.103-Win7',
    'Chrome/51.0.2704.63-Win7',
    'Chrome/60.0.3112.113-Linux',
    'Chrome/48.0.2564.116-Win7',
    'Chrome/54.0.2840.59-Win7',
    'Chrome/61.0.3163.100-',
    'Chrome/45.0.2454.85-Win7',
    'Chrome/60.0.3112.78-Win10',
    'Chrome/24.0.1312.57-Win7',
    'Chrome/58.0.3029.81-Win7',
    'Chrome/60.0.3112.101-Win7',
    'Chrome/43.0.2357.65-Win7',
    'Chrome/48.0.2564.97-Win7',
    'Chrome/60.0.3112.90-Win10',
    'Chrome/49.0.2623.112-',
    'Chrome/57.0.2987.133-Win7',
    'Chrome/60.0.3112.78-Win7',
    'Chrome/25.0.1364.172-Win7',
    'Chrome/58.0.3029.81-Win10',
    'Chrome/60.0.3112.101-Win10',
    'Chrome/49.0.2623.112-Win7',
    'Chrome/60.0.3112.113-',
    'Chrome/45.0.2454.93-Win10',
    'Chrome/49.0.2623.87-',
    'Chrome/54.0.2840.99-',
    'Chrome/58.0.3029.110-',
    'Chrome/51.0.2704.106-Win10',
    'Chrome/43.0.2357.65-',
    'Chrome/47.0.2526.106-Win7',
    'Chrome/49.0.2623.87-Win7',
    'Chrome/49.0.2623.112-Win10',
    'Chrome/59.0.3071.115-Win10',
    'Chrome/60.0.3112.90-',
    'Chrome/26.0.1410.64-Win7',
    'Chrome/48.0.2564.109-',
    'Chrome/53.0.2785.116-Win10',
    'Chrome/53.0.2785.143-Win7',
    'Chrome/51.0.2704.103-Win10',
    'Chrome/59.0.3071.86-Win10',
    'Chrome/41.0.2228.0-Win7',
    'Chrome/48.0.2564.109-Win10',
    'Chrome/54.0.2840.71-Win7',
    'Chrome/60.0.3112.78-Linux',
    'Chrome/51.0.2704.84-Win10',
    'Chrome/58.0.3029.96-Win10',
    'Chrome/54.0.2840.71-Win10',
    'Chrome/62.0.3202.75-Win10',
    'Chrome/53.0.2785.143-Win10',
    'Chrome/47.0.2526.111-Win7',
    'Chrome/52.0.2743.116-Win10',
    'Chrome/57.0.2987.133-',
    'Chrome/60.0.3112.113-Win10',
    'Chrome/52.0.2743.82-Win7',
    'Chrome/50.0.2661.102-Win7',
    'Chrome/59.0.3071.115-Win7',
    'Chrome/58.0.3029.110-Win10',
    'Chrome/46.0.2490.86-',
    'Chrome/46.0.2490.86-Win7',
    'Chrome/48.0.2564.109-Win7',
    'Chrome/59.0.3071.115-Linux',
    'Chrome/61.0.3163.100-Linux',
    'Chrome/41.0.2272.104-Win7',
    'Chrome/49.0.2623.87-Win10',
    'Chrome/47.0.2526.111-Win10',
    'Chrome/62.0.3202.75-',
    'Chrome/50.0.2661.102-Win10',
    'Chrome/44.0.2403.157-Win7',
    'Chrome/51.0.2704.106-Linux',
    'Chrome/46.0.2490.86-Win10',
    'Chrome/62.0.3202.62-Win10',
    'Chrome/62.0.3202.62-Win7',
    'Chrome/39.0.2171.95-Win7',
    'Chrome/59.0.3071.109-',
    'Chrome/47.0.2526.80-Win7',
    'Chrome/62.0.3202.62-Linux',
    'Chrome/48.0.2564.116-',
    'Chrome/45.0.2454.101-Win10',
    'Chrome/55.0.0.12195-Win10',
    'Chrome/46.0.2490.80-Win10',
    'Chrome/55.0.2883.87-Win10',
    'Chrome/62.0.3202.75-Win7',
    'Chrome/56.0.2924.87-',
    'Chrome/46.0.2490.71-Win7',
    'Chrome/50.0.2661.94-Win7',
    'Chrome/45.0.2454.93-Win7',
    'Chrome/51.0.2704.84-Win7',
    'Chrome/50.0.2661.94-Win10',
    'Chrome/51.0.2704.103-',
    'Chrome/59.0.3071.115-',
    'Chrome/62.0.3202.89-Linux',
]



def encrypt(source, key, iv):
    PADDING = "\0"
    pad_it = lambda s: s + (16 - len(s) % 16) * str(PADDING)
    generator = AES.new(key, AES.MODE_CBC, iv)
    crypt = generator.encrypt(pad_it(source))
    return base64.b64encode(crypt)


def decrypt(source, key, iv):
    PADDING = "\0"
    generator = AES.new(key, AES.MODE_CBC, iv)
    recovery = generator.decrypt(base64.b64decode(source))
    return recovery.rstrip(PADDING)


class AccountInsertView(View):
    def post(self, request):
        form = AccountForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.createuser_id = request.user.id
            instance.password = encrypt(request.POST.get('password'), request.user.key[:8] + request.user.iv[8:],
                                        request.user.key[8:] + request.user.iv[:8])
            instance.save()
        return HttpResponseRedirect('/account/account/')


class OthersInsertView(View):
    def post(self, request):
        form = OthersForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.createuser_id = request.user.id
            instance.password = encrypt(request.POST.get('password'), request.user.key[:8] + request.user.iv[8:],
                                        request.user.key[8:] + request.user.iv[:8])
            instance.save()
        return HttpResponseRedirect('/account/others/')


class AccountUploadView(View):
    def post(self, request):
        f = request.FILES['file']
        extension = f.name.split('.')[1]
        if extension != 'csv':
            result = {"ret": 10000, "status": "failed", "msg": u"请选择.csv格式的文件"}
            return HttpResponse(json.dumps(result), content_type="application/json")
        datas = csv.reader(f)
        title = datas.next()
        tag = request.POST.get('tag')
        mode = int(request.POST.get('mode', 0))
        cu = connection.cursor()
        profile = Userprofile.objects.get(id=request.user.id)
        if 'name,email,password,cookies' == ','.join(title):
            items = []
            name = ""
            for line in datas:
                items.append(dict(zip(title, line)))
            try:
                with transaction.atomic():
                    for item in items:
                        if item:
                            new_cookies = []
                            name = item.get('name', '').strip()
                            email = item.get('email', '').strip()
                            password = item.get('password', '').strip()
                            cookies = item.get('cookies', '').strip('"').strip().replace('\\n', ';').strip(";")
                            if cookies:
                                try:
                                    jcookies = json.loads(cookies)
                                    for cookie in jcookies:
                                        jcookie = {}
                                        domain = cookie.get('domain')
                                        expiry = cookie.get('expirationDate',
                                                            cookie.get('Expires', cookie.get('expiry')))
                                        if isinstance(expiry, float):
                                            expiry = str(int(expiry))
                                        if not isinstance(expiry, int):
                                            if not expiry.isdigit():
                                                expiry = str(int(
                                                    time.mktime(
                                                        datetime.strptime(expiry, '%d %b %Y %X GMT').timetuple())))

                                        HttpOnly = cookie.get('hostOnly', cookie.get('HttpOnly', 'false'))
                                        cname = cookie.get('name')
                                        path = cookie.get('path', '/')
                                        secure = cookie.get('secure', 'false')
                                        value = cookie.get('value')
                                        jcookie['Domain'] = domain
                                        jcookie['Expiry'] = expiry
                                        jcookie['Name'] = cname
                                        jcookie['Value'] = value
                                        jcookie['Path'] = path
                                        jcookie['HttpOnly'] = HttpOnly
                                        jcookie['Secure'] = secure
                                        new_cookies.append(jcookie)
                                except Exception as e:
                                    print(e)
                                    lcookies = []
                                    if '\n' in cookies:
                                        lcookies = cookies.split('\n')
                                    elif ';' in cookies:
                                        lcookies = cookies.split(';')
                                    for cookie in lcookies:
                                        jcookie = {}
                                        c = cookie.strip()
                                        if '\t' in c:
                                            c = c.split('\t')
                                        elif ' ' in c:
                                            c = c.split(' ')
                                        expiry = c[4]
                                        jcookie['Domain'] = c[0]
                                        jcookie['Expiry'] = expiry
                                        jcookie['Name'] = c[5]
                                        jcookie['Value'] = c[6]
                                        jcookie['Path'] = c[2]
                                        jcookie['HttpOnly'] = c[1]
                                        jcookie['Secure'] = c[3]
                                        new_cookies.append(jcookie)
                            new_cookies = json.dumps(json.loads(json.dumps(new_cookies)))
                            password = encrypt(password, profile.key[:8] + profile.iv[8:],
                                               profile.key[8:] + profile.iv[:8])
                            if mode == 0:
                                sql = 'insert into account(name,email,password,cookies,tag_id,createtime,createuser_id,enable_cookie,enable_review,review_flag) values (%s,%s,%s,%s,%s,%s,%s,0,0,0)'
                                cu.execute(sql, (
                                    name, email, password, new_cookies, tag,
                                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                    request.user.id))
                            elif mode == 1:
                                sql = 'update account set email=%s,password=%s,cookies=%s,updatetime=%s,updateuser_id=%s where name=%s and tag_id=%s and createuser_id=%s'
                                cu.execute(sql, (
                                    email, password, new_cookies, datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                    request.user.id,
                                    name, tag, request.user.id))
            except IntegrityError:
                result = {"ret": 10001, "status": "failed", "msg": u"账号:%s 已存在" % name}
                return HttpResponse(json.dumps(result), content_type="application/json")

            except Exception, ex:
                result = {"ret": 10001, "status": "failed", "msg": u"账号:%s出错,出错原因:%s" % (name, str(ex))}
                return HttpResponse(json.dumps(result), content_type="application/json")
            result = {"ret": 0, "status": "success"}
            # Log.objects.create(user_id=request.user.id, ctype=1, operation=1, desc=u"批量导入账号,批次号为:%s" % batchno)
        else:
            result = {"ret": 10000, "status": "failed", "msg": u"文件格式错误,标题应该为 name,email,password,cookies"}
        return HttpResponse(json.dumps(result), content_type="application/json")


class OthersUploadView(View):
    def post(self, request):
        f = request.FILES['file']
        extension = f.name.split('.')[1]
        if extension != 'csv':
            result = {"ret": 10000, "status": "failed", "msg": u"请选择.csv格式的文件"}
            return HttpResponse(json.dumps(result), content_type="application/json")
        datas = csv.reader(f)
        title = datas.next()
        tag = request.POST.get('tag')
        proxy = Tag.objects.get(id=tag).proxy
        browser = random.choice(browser_list)
        mode = int(request.POST.get('mode', 0))
        cu = connection.cursor()
        profile = Userprofile.objects.get(id=request.user.id)
        if 'name,email,password,cookies' == ','.join(title):
            items = []
            name = ""
            for line in datas:
                items.append(dict(zip(title, line)))
            try:
                with transaction.atomic():
                    for item in items:
                        if item:
                            new_cookies = []
                            name = item.get('name', '').strip()
                            email = item.get('email', '').strip()
                            password = item.get('password', '').strip()
                            cookies = item.get('cookies', '').strip('"').strip().replace('\\n', ';').strip(";")
                            if cookies:
                                try:
                                    jcookies = json.loads(cookies)
                                    for cookie in jcookies:
                                        jcookie = {}
                                        domain = cookie.get('domain')
                                        expiry = cookie.get('expirationDate',
                                                            cookie.get('Expires', cookie.get('expiry')))
                                        if isinstance(expiry, float):
                                            expiry = str(int(expiry))
                                        if not isinstance(expiry, int):
                                            if not expiry.isdigit():
                                                expiry = str(int(
                                                    time.mktime(
                                                        datetime.strptime(expiry, '%d %b %Y %X GMT').timetuple())))

                                        HttpOnly = cookie.get('hostOnly', cookie.get('HttpOnly', 'false'))
                                        cname = cookie.get('name')
                                        path = cookie.get('path', '/')
                                        secure = cookie.get('secure', 'false')
                                        value = cookie.get('value')
                                        jcookie['Domain'] = domain
                                        jcookie['Expiry'] = expiry
                                        jcookie['Name'] = cname
                                        jcookie['Value'] = value
                                        jcookie['Path'] = path
                                        jcookie['HttpOnly'] = HttpOnly
                                        jcookie['Secure'] = secure
                                        new_cookies.append(jcookie)
                                except Exception as e:
                                    print(e)
                                    lcookies = []
                                    if '\n' in cookies:
                                        lcookies = cookies.split('\n')
                                    elif ';' in cookies:
                                        lcookies = cookies.split(';')
                                    for cookie in lcookies:
                                        jcookie = {}
                                        c = cookie.strip()
                                        if '\t' in c:
                                            c = c.split('\t')
                                        elif ' ' in c:
                                            c = c.split(' ')
                                        expiry = c[4]
                                        jcookie['Domain'] = c[0]
                                        jcookie['Expiry'] = expiry
                                        jcookie['Name'] = c[5]
                                        jcookie['Value'] = c[6]
                                        jcookie['Path'] = c[2]
                                        jcookie['HttpOnly'] = c[1]
                                        jcookie['Secure'] = c[3]
                                        new_cookies.append(jcookie)
                            new_cookies = json.dumps(json.loads(json.dumps(new_cookies)))
                            password = encrypt(password, profile.key[:8] + profile.iv[8:],
                                               profile.key[8:] + profile.iv[:8])

                            if mode == 0:
                                sql = 'insert into others(name,email,password,cookies,tag_id,createtime,createuser_id,proxy,browser,status) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                                cu.execute(sql, (
                                    name, email, password, new_cookies, tag,
                                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                    request.user.id, 'ZZ', browser, 'Y'))
                            elif mode == 1:
                                sql = 'update others set email=%s,password=%s,cookies=%s,updatetime=%s,updateuser_id=%s where name=%s and tag_id=%s and createuser_id=%s'
                                cu.execute(sql, (
                                    email, password, new_cookies, datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                    request.user.id,
                                    name, tag, request.user.id))
            except IntegrityError:
                result = {"ret": 10001, "status": "failed", "msg": u"账号:%s 已存在" % name}
                return HttpResponse(json.dumps(result), content_type="application/json")

            except Exception, ex:
                result = {"ret": 10001, "status": "failed", "msg": u"账号:%s出错,出错原因:%s" % (name, str(ex))}
                return HttpResponse(json.dumps(result), content_type="application/json")
            result = {"ret": 0, "status": "success"}
            # Log.objects.create(user_id=request.user.id, ctype=1, operation=1, desc=u"批量导入账号,批次号为:%s" % batchno)
        else:
            result = {"ret": 10000, "status": "failed", "msg": u"文件格式错误,标题应该为 name,email,password,cookies"}
        return HttpResponse(json.dumps(result), content_type="application/json")


class GetListView(View):
    def get(self, request):
        account = Account.objects.filter(enable_review=0, createuser=request.user)
        resp = []
        for a in account:
            data = {'name': a.name, 'email': a.email, 'cookies': a.cookies}
            resp.append(data)
        return HttpResponse(json.dumps(resp), content_type="application/json")
