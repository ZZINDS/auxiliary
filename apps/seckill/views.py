# coding=utf-8
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django.views.generic import View

from .models import Seckill
from .forms import SeckillForm


class InsertView(View):
    def get(self, request):
        pass

    def post(self, request):
        form = SeckillForm(request.POST)
        begin_time = request.POST.get('starttime1')
        end_time = request.POST.get('starttime2')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.begin_time = begin_time
            instance.end_time = end_time
            instance.save()

        return HttpResponseRedirect('/seckill/seckill/')


class SeckillView(View):
    def get(self, request):
        now = datetime.now()

        task = Seckill.objects.filter(begin_time__lte=now, end_time__gte=now).exclude(status='stop').exclude(
            status='end')
        resp = []
        for t in task:
            data = {
                'url': 'https://' + t.tag.domain + '/dp/' + t.asin,
                'asin': t.asin,
                'tag': t.tag.site,
                'kill_percent': t.kill_percent,
                'now_percent': t.now_percent,
                'count': t.count,
                'status': t.status
            }
            resp.append(data)
        return HttpResponse(json.dumps(resp), content_type="application/json")


# ?asin=xxx&status=xxx&kill_percen
class SeckillStatus(View):
    def get(self, request):
        asin = request.GET.get('asin', '')
        status = request.GET.get('status', '')
        now_percent = request.GET.get('now_percent', '')
        hours = request.GET.get('hours', '')
        if status == 'end':
            Seckill.objects.filter(asin=asin).update(status='end')
        else:
            cartlist = Seckill.objects.filter(asin=asin)
            for cart in cartlist:
                cart.count += 1
                cart.now_percent = now_percent
                cart.hours = hours
                cart.status = 'process'
                cart.save()
        return HttpResponse('ok')

    def post(self, request):
        asin = request.POST.get('asin', '')
        status = request.POST.get('status', '')
        now_percent = request.POST.get('now_percent', '')
        hours = request.POST.get('hours', '')
        if status == 'end':
            Seckill.objects.filter(asin=asin).update(status='end')
        else:
            cartlist = Seckill.objects.filter(asin=asin)
            for cart in cartlist:
                cart.count += 1
                cart.now_percent = now_percent
                cart.hours = hours
                cart.status = 'process'
                cart.save()
        return HttpResponse('ok')
