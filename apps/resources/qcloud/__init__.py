from django.conf import settings
from tencentcloud.common import credential

# 获取密钥
def getCredential():
    return credential.Credential(settings.QCLOUD_SECRETID, settings.QCLOUD_SECRETKEY)