from django.shortcuts import render
from idc.models import Idc
from django.http import JsonResponse, QueryDict, HttpResponse
from idc.serializers import IdcSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



# Create your views here.


# def idc_list(request):
#     if request.method == 'GET':
#         ret = []
#         idc_list = Idc.objects.all()
#         for idc in idc_list:
#             ret.append({'name': idc.name, 'address': idc.address, 'phone': idc.phone, 'email': idc.email})
#         return JsonResponse(ret, safe=False)
#
#     elif request.method == 'POST':
#         name = request.POST['name']
#         address = request.POST['address']
#         phone = request.POST['phone']
#         email = request.POST['email']
#
#         idc = Idc.objects.create(
#             name=name,
#             address=address,
#             phone=phone,
#             email=email
#         )
#         ret = {'msg': '创建IDC %s 成功' % idc.name}
#         return JsonResponse(ret)


# class JsonResponse(HttpResponse):
#
#     def __init__(self, data, **kwargs):
#         kwargs.setdefault('content_type', 'application/json')
#         content = JSONRenderer().render(data.data)
#         super(JsonResponse, self).__init__(content=content, **kwargs)


class JsonResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        kwargs.setdefault('content_type', 'application/json')
        content = JSONRenderer().render(data)
        super(JsonResponse, self).__init__(content=content, **kwargs)


def idc_list(request):
    if request.method == "GET":
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset, many=True)
        return JsonResponse(serializer.data)
    elif request.method == "POST":
        content = JSONParser().parse(request)
        idc_serializer = IdcSerializer(data=content)
        if idc_serializer.is_valid():
            idc_serializer.save()
            return JsonResponse(idc_serializer.data)


# def idc_detail(request, pk):
#     if request.method == "GET":
#         idc = Idc.objects.get(id=pk)
#         ret = {'name': idc.name, 'address': idc.address, 'phone': idc.phone, 'email': idc.email}
#         return JsonResponse(ret)
#     elif request.method == "PUT":
#         body = request.body
#         quer_body = QueryDict(body)
#         Idc.objects.filter(id=pk).update(
#             name=quer_body['name'],
#             address=quer_body['address'],
#             phone=quer_body['phone'],
#             email=quer_body['email'],
#         )
#         ret = {'msg': '修改成功'}
#         return JsonResponse(ret)
#     elif request.method == "DELETE":
#         Idc.objects.get(id=pk).delete()
#         ret = {'msg': '删除成功'}
#         return JsonResponse(ret)


def idc_detail(request, pk):
    try:
        idc = Idc.objects.get(id=pk)
    except Idc.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = IdcSerializer(idc)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        content = JSONParser().parse(request)
        idc_serializer = IdcSerializer(idc, data=content)
        if idc_serializer.is_valid():
            idc_serializer.save()
            return JsonResponse(idc_serializer.data)
    elif request.method == "DELETE":
        idc.delete()
        return HttpResponse(status=204)

######################### 版本二 #########################

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(["GET", "POST"])
def idc_list_v2(request):
    if request.method == "GET":
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        content = JSONParser().parse(request)
        idc_serializer = IdcSerializer(data=content)
        if idc_serializer.is_valid():
            idc_serializer.save()
            return Response(idc_serializer.data, status=status.HTTP_201_CREATED)
        return Response(idc_serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "DELETE", "PUT"])
def idc_detail_v2(request, pk):
    try:
        idc = Idc.objects.get(id=pk)
    except Idc.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = IdcSerializer(idc)
        return Response(serializer.data)
    elif request.method == "PUT":
        content = JSONParser().parse(request)
        idc_serializer = IdcSerializer(idc, data=content)
        if idc_serializer.is_valid():
            idc_serializer.save()
            return Response(idc_serializer.data)
        return Response(idc_serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        idc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def api_root(request, format=None, *args, **kwargs):
    return Response({
        "idcs": reverse('idc_list', request=request, format=format)
    })

######################### 版本三 #########################

from rest_framework.views import APIView
from django.http import Http404


class IdcListView(APIView):

    def get(self, request, format=None):
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # content = JSONParser().parse(request)
        serializer = IdcSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class IdcDetailView(APIView):

    def get_object(self, pk):
        try:
            return Idc.objects.get(id=pk)
        except Idc.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        idc = self.get_object(pk)
        serializer = IdcSerializer(idc)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        idc = self.get_object(pk)
        serailizer = IdcSerializer(idc, data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.context)
        return Response(serailizer.context, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        idc = self.get_object(pk)
        idc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

######################### 版本四 #########################

from rest_framework import mixins, generics


class IdcListViewV4(generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class IdcDetailViewV4(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

######################### 版本五 #########################

class IdcListViewV5(generics.ListCreateAPIView):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer


class IdcDetailViewV5(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

######################### 版本六 #########################

from rest_framework import viewsets


class IdcViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.RetrieveModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

######################### 版本七 #########################

from rest_framework.pagination import PageNumberPagination

class IdcViewSetV7(viewsets.ModelViewSet):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer
    pagination_class = PageNumberPagination
