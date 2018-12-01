# _*_ coding: utf-8 _*_
__author__ = 'HeYang'
from django.conf.urls import url, include
from idc.views import *

urlpatterns = [
    url(r'^$',idc_list , name='idc_list'),
    url(r'(?P<pk>\d)/$', idc_detail, name='idc_detail'),
]

######################### 版本二 #########################

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', api_root),
    url(r'^idcs/$',idc_list_v2 , name='idc_list'),
    url(r'^idcs/(?P<pk>\d)/$', idc_detail_v2, name='idc_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

######################### 版本三 #########################

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', api_root),
    url(r'^idcs/$', IdcListView.as_view() , name='idc_list'),
    url(r'^idcs/(?P<pk>\d)/$', IdcDetailView.as_view(), name='idc_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

######################### 版本四 #########################

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', api_root),
    url(r'^idcs/$', IdcListViewV4.as_view() , name='idc_list'),
    url(r'^idcs/(?P<pk>\d)/$', IdcDetailViewV4.as_view(), name='idc_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

######################### 版本五 #########################

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', api_root),
    url(r'^idcs/$', IdcListViewV5.as_view() , name='idc_list'),
    url(r'^idcs/(?P<pk>\d)/$', IdcDetailViewV5.as_view(), name='idc_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

######################### 版本六 #########################

idc_list = IdcViewSet.as_view({
    "get": "list",
    "post": "create"
})

idc_detail = IdcViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "delete": "destroy",
})

urlpatterns = [
    url(r'^$', api_root),
    url(r'^idcs/$', idc_list, name='idc_list'),
    url(r'^idcs/(?P<pk>\d)/$', idc_detail, name='idc_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

######################### 版本七 #########################

from rest_framework.routers import DefaultRouter
from users.views import *

route = DefaultRouter()
route.register("idcs", IdcViewSetV7)
route.register("users", UsersView)

urlpatterns = [
    url(r'^', include(route.urls)),
]