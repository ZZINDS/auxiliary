# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 上午10:12
# @Author  : sing

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World"]
