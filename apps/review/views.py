# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from .models import Task, Queue
from .forms import TaskForm
from datetime import datetime
from account.models import *


class InsertView(View):
    def post(self, request):
        # rank = None
        # sid = request.POST.get('id')
        begin = request.POST.get('time_begin', 0)
        end = request.POST.get('time_end', 0)
        starttime = request.POST.get('starttime1')
        form = TaskForm(request.POST)
        # if int(begin) > int(end):
        #     result = {"status": "fail", "msg": "评论间隔的开始时间不能大于结束时间"}
        #     return HttpResponse(json.dumps(result), content_type="application/json")
        comment = request.POST.get("comment")
        comments = comment.strip().strip('\r\n').split('\r\n')
        for com in comments:
            if '|' not in com:
                result = {"status": "fail", "msg": "请输入正确的评论格式(标点符号为英文符号),错误的评论为:%s" % com}
                return HttpResponse(json.dumps(result), content_type="application/json")
        total = request.POST.get('total')
        # if int(total) > len(comments):
        # result = {"status": "fail", "msg": "输入的评论总数(%s)大于设置的评论条数(%s)!" % (1, len('2'))}
        # return HttpResponse(json.dumps(result), content_type="application/json")
        if form.is_valid():
            instance = form.save(commit=False)
            instance.start = begin
            instance.end = end
            instance.updateuser = request.user
            instance.createuser = request.user
            instance.starttime = starttime
            instance.save()

        return HttpResponseRedirect('/review/task/')


class AllocateView(View):
    def get(self, request):
        task = Task.objects.filter(sync_flag=False, finish=False, starttime__lte=datetime.now()).all()
        for t in task:
            comments = t.comment.strip().strip('\r\n').split('\r\n')
            for com in comments:
                l_comment = com.split("|")
                title = l_comment[0]
                content = l_comment[1]
                if not title:
                    title = "five star"
                if not content:
                    content = "amazing"
                queue = Queue()
                queue.task = t
                queue.tag = t.tag
                queue.asin = t.asin
                queue.title = title
                queue.content = content
                queue.name_type = t.name_type
                queue.createuser = t.createuser
                queue.createtime = datetime.now()
                queue.starttime = t.starttime
                queue.save()
            t.sync_flag = True
            t.save()
        return HttpResponse(task)


class GetListView(View):
    def get(self, request):
        queue = Queue.objects.filter(status=0, starttime__lte=datetime.now())
        resp = []
        for q in queue:
            account = Account.objects.filter(enable_review=0, createuser=q.createuser)
            if not account:
                break
            al = []
            for a in account:
                data = {'name': a.name, 'email': a.email, 'cookies': a.cookies, 'account_id': a.id}
                al.append(data)
            data = {
                'queue_id': q.id,
                'asin': q.asin,
                'title': q.title,
                'content': q.content,
                'name_type': q.name_type,
                'url': q.tag.url,
                'account': al
            }
            resp.append(data)
        return HttpResponse(json.dumps(resp), content_type="application/json")


class PostView(View):
    def post(self, request):
        account_id = request.POST.get('account_id')
        queue_id = request.POST.get('queue_id')
        reviewId = request.POST.get('reviewId')
        account = Account.objects.get(id=account_id)
        if len(reviewId) == 3:
            account.enable_review = reviewId
        else:
            account.review_flag = True
            queue = Queue.objects.get(id=queue_id)
            queue.account = account
            queue.reviewtime = datetime.now()
            queue.reviewid = reviewId
            queue.status = True
            queue.save()

            q_task = Queue.objects.filter(task=queue.task)
            finish_flag = True
            task_id = 0
            for q in q_task:
                task_id = q.task_id
                if not q.status:
                    finish_flag = False
                    break
            if finish_flag:
                task = Task.objects.get(id=task_id)
                task.finish = True
                task.save()

        account.save()
        return HttpResponse('ok')
