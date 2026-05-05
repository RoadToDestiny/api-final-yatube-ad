from rest_framework import permissions


class IsAuthenticatedForFollow(permissions.BasePermission):
    """
    Разрешение, требующее аутентификации для доступа к /follow/ эндпоинту.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение, позволяющее только автору редактировать и удалять объект.
    Остальным пользователям - только чтение.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
