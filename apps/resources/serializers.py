from rest_framework import serializers
from .models import Server, Cloud, Ip
import datetime

class ServerSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    cloud = serializers.PrimaryKeyRelatedField(queryset=Cloud.objects.all())
    instanceId = serializers.CharField(required=True)
    instanceType = serializers.CharField(required=True)
    cpu = serializers.CharField(required=True)
    memory = serializers.CharField(required=True)
    instanceName = serializers.CharField(required=True)
    createdTime = serializers.DateTimeField(required=True, format="%Y-%m-%d %H:%M:%S")
    expiredTime = serializers.DateTimeField(required=True, format="%Y-%m-%d %H:%M:%S")
    hostname = serializers.CharField(required=True)
    publicIps = serializers.ListField(required=True, write_only=True)
    innerIps = serializers.ListField(required=True, write_only=True)

    def get_cloud(self, code):
        object = Cloud.objects.get(code=code)
        return object

    def to_internal_value(self, data):
        data['cloud'] = self.get_cloud(data['cloud']).id
        return super(ServerSerializer, self).to_internal_value(data)

    def get_object(self, instanceId):
        try:
            object = Server.objects.get(instanceId=instanceId)
            return object
        except Exception as e:
            return None

    def create(self, validated_data):
        object = self.get_object(validated_data.get('instanceId'))
        if object:
            return self.update(object, validated_data)
        publicIps = validated_data.pop('publicIps')
        innerIps = validated_data.pop('innerIps')
        object = Server.objects.create(**validated_data)
        try:
            self.check_publicIps(object, publicIps)
            self.check_innerIps(object, innerIps)
        except Exception as e:
            print(e)
        return object

    def check_publicIps(self, object, publicIps):
        object_list = object.publicIpAddress.all()
        current_ip = []
        for ip in publicIps:
            try:
                ip_obj = object.publicIpAddress.get(ip=ip)
            except Ip.DoesNotExist:
                ip_obj = Ip.objects.create(ip=ip, public=object)
            current_ip.append(ip_obj)
        no_exits_list = list(set(object_list) - set(current_ip))
        for ip_obj in no_exits_list:
            ip_obj.delete()

    def check_innerIps(self, object, innerIps):
        object_list = object.innerIpAddress.all()
        current_ip = []
        for ip in innerIps:
            try:
                ip_obj = object.innerIpAddress.get(ip=ip)
            except Exception as e:
                ip_obj = Ip.objects.create(ip=ip, inner=object)
            current_ip.append(ip_obj)
        no_exits_list = list(set(object_list) - set(current_ip))
        for ip_obj in no_exits_list:
            ip_obj.delete()

    def update(self, instance, validated_data):
        instance.cpu = validated_data.get('cpu')
        instance.instanceName = validated_data.get('instanceName')
        self.check_publicIps(instance, validated_data.get('publicIps'))
        self.check_innerIps(instance, validated_data.get('innerIps'))
        instance.save()
        return instance

    def to_representation(self, instance):
        ret = super(ServerSerializer, self).to_representation(instance)
        ret['cloud'] = {
            'id': instance.cloud.id,
            'name': instance.cloud.name,
            'code': instance.cloud.code
        }
        ret['publicIps'] = [ip.ip for ip in instance.publicIpAddress.all()]
        ret['innerIps'] = [ip.ip for ip in instance.innerIpAddress.all()]
        createdTime = datetime.datetime.strptime(ret['createdTime'], "%Y-%m-%d %H:%M:%S")
        expiredTime = datetime.datetime.strptime(ret['expiredTime'], "%Y-%m-%d %H:%M:%S")
        ret['createdTime'] = (createdTime + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
        ret['expiredTime'] = (expiredTime + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
        return ret
    # class Meta:
    #     model = Server
    #     fields = "__all__"