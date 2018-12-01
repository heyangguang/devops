# _*_ coding: utf-8 _*_
__author__ = 'HeYang'
from django.http import HttpResponse
import json

def test_url(request, *args, **kwargs):
    return HttpResponse(json.dumps(args))


def test_url2(request, *args, **kwargs):
    return HttpResponse(json.dumps(kwargs))