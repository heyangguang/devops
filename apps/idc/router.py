from rest_framework.routers import DefaultRouter
from .views import IdcViewSetV7

idc_router = DefaultRouter()
idc_router.register(r'idc', IdcViewSetV7)