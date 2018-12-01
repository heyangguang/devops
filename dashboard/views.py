from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
import logging

User = get_user_model()

logger = logging.getLogger(__name__)
# Create your views here.

def index(request):
    data = '111'
    return HttpResponse(data)


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('index view')


# 获取 增加 删除 修改 用户
def user(request):
    if request.method == 'GET':
        return HttpResponse('获取用户信息')
    elif request.method == 'POST':
        return HttpResponse('修改用户信息')
    elif request.method == 'PUT':
        return HttpResponse('增加用户信息')
    elif request.method == 'DELETE':
        return HttpResponse('删除用户信息')
    return HttpResponse('')


class UserView(View):

    def get(self, request, *args, **kwargs):
        try:
            page = int(request.GET.get('page'))
        except Exception:
            page = 1

        if page < 1:
            page = 1

        per = 10
        end = page * per
        start = end - per

        queryset = User.objects.all()[start:end]
        data = [{'id': user.id, 'username': user.username} for user in queryset]
        return JsonResponse(data, safe=False)

    def post(self, request, *args, **kwargs):
        return HttpResponse('修改用户信息')

    def put(self, request, *args, **kwargs):
        return HttpResponse('增加用户信息')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('删除用户信息')


class UserView2(View):

    def get(self, request, *args, **kwargs):
        p = Paginator(User.objects.all(), 10)
        try:
            page = int(request.GET.get('page'))
        except Exception:
            page = 1

        if page < 1:
            page = 1
        data = p.page(page)
        data = [{"id": user.id, "username": user.username} for user in data.object_list]
        logger.debug('查询用户')
        return JsonResponse(data, safe=False)

    def post(self, request, *args, **kwargs):
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.create_user(username=username, email=email, password=password)
            logger.info('创建用户成功')
            return JsonResponse('创建 %s 用户成功' %(user.username), safe=False)
        except Exception:
            logger.error('创建用户失败')
            return JsonResponse('数据格式有问题,创建失败', safe=False)

    def put(self, request, *args, **kwargs):
        return HttpResponse('增加用户信息')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('删除用户信息')
