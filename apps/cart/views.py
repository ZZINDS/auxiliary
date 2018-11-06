# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#import jsom
from django.shortcuts import render

# Create your views here.

from django.views.generic import View
from .models import Cart
#from .models import Cart_allocation
from django.http import HttpResponseRedirect
#from account.models import *


class InsertView(View):
    def post(self, request):
        tag = request.POST.get('tag', 0)
        option = int(request.POST.get('option'))
        asin =request.POST.get('asin')
        keyword = request.POST.get('keyword')
        sellerid =request.POST.get('sellerid')
        brand = request.POST.get('brand')
        total = int(request.POST.get('total'))
        wish = int(request.POST.get('wish'))
        starttime = request.POST.get('starttime1')
        updateuser = request.user
        createuser = request.user
        cart = Cart()
        cart.tag_id = tag
        cart.option = option
        cart.asin = asin
        cart.keyword = keyword
        cart.sellerid = sellerid
        cart.brand = brand
        cart.total = total
        cart.wish = wish
        cart.starttime = starttime
        cart.createuser = createuser
        cart.updateuser = updateuser
        cart.save()
        return HttpResponseRedirect('/cart/cart')

#class AllocateView(View):
#    def get(self, request):
#        cart = Cart.objects.filter(sync_flag=False,finish=False,starttime__lte=datetinm.now()).all()
#        for i in cart:
#            comments  = i.c