from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth.models import Group, Permission
from rest_framework import viewsets, generics, status, mixins
from rest_framework.response import Response
from users.serializers import UserSerializer, GroupSerializer, PermissionSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import UserFilter
from django.contrib.auth import get_user_model

# Create your views here.


# class UserAllView(View):
#
#     def get(self, request):
#         user_all = User.objects.all().values_list()
#         return JsonResponse(list(user_all), safe=False)
#
#
# class GroupGetUserView(View):
#
#     def get(self, request):
#         group_id = request.GET.get('id')
#         group_get_user = Group.objects.get(pk=group_id).user_set.all().values_list()
#         return JsonResponse(list(group_get_user), safe=False)
#
#
# class UserGetGroupView(View):
#
#     def get(self, request):
#         user_name = request.GET.get('name')
#         print(user_name)
#         user_get_group = User.objects.get(username=user_name).groups.all().values_list()
#         return JsonResponse(list(user_get_group), safe=False)
#
#
# class UserAddGroupView(View):
#
#     def post(self, request):
#         data = {'status': '添加成功'}
#         username = request.POST.get('username')
#         groupname = request.POST.get('groupname')
#         try:
#
#             u = User.objects.get(username=username).groups.add(Group.objects.get(name=groupname))
#             data['data'] = u.username
#         except Exception:
#             data['status'] = '添加失败'
#         return JsonResponse(data)
#
#
# class UserDeleteGroupView(View):
#
#     def post(self, request):
#         data = {'status': 'T出成功'}
#         username = request.POST.get('username')
#         groupname = request.POST.get('groupname')
#         try:
#             User.objects.get(username=username).groups.clear()
#             data['这个组还有那些用户'] = list(Group.objects.get(groupname=groupname).user_set.all().values_list())
#         except Exception:
#             data['status'] = 'T出失败'
#         return JsonResponse(data)
User = get_user_model()

class UsersView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = UserFilter
    filter_fields = ("username",)


class UserGroupsView(viewsets.ViewSet, generics.GenericAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        content = self.get_queryset().get(**filter_kwargs)
        return content

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_object().groups.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        UserObj = self.get_object()
        GroupObj = Group.objects.get(id=request.data.get('gid'))
        UserObj.groups.remove(GroupObj)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        UserObj = User.objects.get(id=request.data.get('uid'))
        GroupObj = Group.objects.get(id=request.data.get('gid'))
        UserObj.groups.add(GroupObj)
        return Response(status=status.HTTP_201_CREATED)


class GroupView(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class GroupUsersView(viewsets.ViewSet, generics.GenericAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = Group.objects.all()
        return queryset

    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        content = self.get_queryset().get(**filter_kwargs)
        return content

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_object().user_set.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        GroupObj = self.get_object()
        UserObj = User.objects.get(id=request.data.get('uid'))
        GroupObj.user_set.add(UserObj)
        return Response(status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        GroupObj = Group.objects.get(id=request.data.get('gid'))
        UserObj = User.objects.get(id=request.data.get('uid'))
        GroupObj.user_set.remove(UserObj)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PermissionView(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class GroupPermissionView(viewsets.ViewSet, generics.GenericAPIView):
    pass