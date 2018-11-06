# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from .models import Tag
from django.http import HttpResponseRedirect
from .forms import TagForm
from .models import Tag


class InsertView(View):
    def post(self, request):
        form = TagForm(data=request.POST)
        name = request.POST.get('name')
        url = request.POST.get('url')
        tag = Tag.objects.filter(name=name)
        if tag:
            tag.update(url=url)
        else:
            form.save()
        return HttpResponseRedirect('/tags/tag')
