from django.db import models

# Create your models here.


class Idc(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='idc名称')
    address = models.CharField(max_length=200, verbose_name='idc地址')
    phone = models.CharField(max_length=20, null=True, verbose_name='idc的联系电话')
    email = models.CharField(max_length=50, null=True, verbose_name='idc的email地址')
    status_list = [
        (0, 'enabled'),
        (1, 'disabled')
    ]
    status = models.BooleanField(choices=status_list, default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'idc'