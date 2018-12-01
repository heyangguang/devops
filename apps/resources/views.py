from django.http import HttpResponse
from django.views.generic import View
from .qcloud import cvm
from rest_framework import mixins, viewsets
from .serializers import ServerSerializer
from .models import Server
from resources.apscheduler import scheduler

def rundata():
    cvm.getCvmList()
    print('更新完成')

class TestView(View):

    def get(self, request):
        cvm.getCvmList()
        # scheduler.add_job(rundata,'interval', seconds=10)
        # scheduler.start()
        return HttpResponse('')


class ServerListView(viewsets.GenericViewSet,
                     mixins.ListModelMixin):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer