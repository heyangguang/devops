"""devops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from resources.router import servers_router
from users.router import user_router, group_router, perm_router
from idc.router import idc_router
# from resources.apscheduler import scheduler

route = DefaultRouter()
route.registry.extend(servers_router.registry)
route.registry.extend(user_router.registry)
route.registry.extend(group_router.registry)
route.registry.extend(idc_router.registry)
route.registry.extend(perm_router.registry)

urlpatterns = [
    url(r'^', include(route.urls)),
    url(r'^', include('resources.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^doc/', include_docs_urls(title='syscmdb系统API')),
]

