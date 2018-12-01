# _*_ coding: utf-8 _*_
__author__ = 'HeYang'
from django.conf.urls import url
from dashboard.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'index_view', IndexView.as_view(), name='index_view'),
    url(r'user/$', UserView2.as_view(), name='user_view'),
]