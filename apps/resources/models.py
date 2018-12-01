from django.db import models


class Cloud(models.Model):
    name = models.CharField(max_length=50, verbose_name='云厂商名称')
    code = models.CharField(max_length=25, verbose_name='云厂商简称')

    def __str__(self):
        return self.name


class Server(models.Model):
    cloud = models.ForeignKey(Cloud)
    instanceId = models.CharField(max_length=100, verbose_name='实例ID', db_index=True)
    instanceType = models.CharField(max_length=20, verbose_name='实例类型')
    cpu = models.CharField(max_length=32, verbose_name='cpu')
    memory = models.CharField(max_length=32, verbose_name='memory')
    instanceName = models.CharField(max_length=32, verbose_name='实例名称', db_index=True)
    createdTime = models.DateTimeField(verbose_name='实例创建时间')
    expiredTime = models.DateTimeField(verbose_name='实例到期时间')
    hostname = models.CharField(max_length=32, verbose_name='主机名')


class Ip(models.Model):
    ip = models.GenericIPAddressField(db_index=True)
    inner = models.ForeignKey(Server, related_name='innerIpAddress', verbose_name='内网IP', null=True)
    public = models.ForeignKey(Server, related_name='publicIpAddress', verbose_name='外网IP', null=True)