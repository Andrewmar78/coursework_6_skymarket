from rest_framework import permissions
from backend.users.models import User


class UserPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        """Проверка аутентификации пользователя для создания объекта"""
        if view.action == 'create':
            return request.user.is_authenticated
        else:
            return True

    def has_object_permission(self, request, view, obj):
        """Проверка авторизации, автора объекта или админа для изменения объекта"""
        if not request.user.is_authenticated:
            return False
        if view.action in ['update', 'partial_update', 'destroy']:
            return obj.author == request.user or request.user.role == User.ADMIN
        if view.action == 'retrieve':
            return True
        else:
            return False
