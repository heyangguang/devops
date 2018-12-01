from rest_framework.routers import DefaultRouter
from .views import UsersView, GroupView, UserGroupsView, GroupUsersView, PermissionView

user_router = DefaultRouter()
user_router.register(r'user', UsersView)
user_router.register(r'userGroup', UserGroupsView, base_name='user_group')

group_router = DefaultRouter()
group_router.register(r'group', GroupView)
group_router.register(r'groupUser', GroupUsersView, base_name='group_user')

perm_router = DefaultRouter()
perm_router.register(r'perm', PermissionView)