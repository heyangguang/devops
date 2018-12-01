# _*_ coding: utf-8 _*_
__author__ = 'HeYang'
from rest_framework import serializers
from idc.models import Idc


class IdcSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, help_text='id')
    name = serializers.CharField(required=False, help_text='IDC名称', label="IDC名称")
    address = serializers.CharField(required=False, help_text='IDC地址', label="IDC地址")
    phone = serializers.CharField(required=False, help_text='IDC联系电话', label="IDC联系电话")
    email = serializers.CharField(required=False, help_text='IDC邮箱email', label="IDC邮箱email")
    status = serializers.IntegerField(required=False, help_text='状态', label='状态')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.status = validated_data.get('status', instance.status)
        print(validated_data.get('status'))
        instance.save()
        return instance

    def create(self, validated_data):
        return Idc.objects.create(**validated_data)


    def to_internal_value(self, data):
        # 反序列化的第一步
        print(data)
        return super(IdcSerializer, self).to_internal_value(data)


    def to_representation(self, instance):
        # 序列化的最后一步
        instance = super(IdcSerializer, self).to_representation(instance)
        # instance['test'] = 'aaa'
        return instance