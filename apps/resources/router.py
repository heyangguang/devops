from rest_framework.routers import DefaultRouter
from .views import ServerListView

servers_router = DefaultRouter()
servers_router.register(r'server/list', ServerListView, base_name='server_list')