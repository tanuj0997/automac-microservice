from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsSuperAdminUser(IsAdminUser):
    def has_permission(self, request, view):
        return (
            True
            if request.user.is_authenticated and request.user.is_superuser
            else False
        )
