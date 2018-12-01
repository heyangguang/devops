from django.db import models

# Create your models here.


class Idc(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='idc名称')
    address = models.CharField(max_length=200, verbose_name='idc地址')
    phone = models.CharField(max_length=20, null=True, verbose_name='idc的联系电话')
    user = models.CharField(max_length=32, null=True, verbose_name='idc的联系人')


class ZhiZao(models.Model):
    name = models.CharField(max_length=32, verbose_name='制造商')

    def __str__(self):
        return self.name

class Car(models.Model):
    zhizao = models.ForeignKey(ZhiZao)
    name = models.CharField(max_length=32, verbose_name='型号')

    def __str__(self):
        return self.name