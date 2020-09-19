from rest_framework.permissions import IsAdminUser


class IsSuperAdminUser(IsAdminUser):
    """
    Checked the permission and authenticate the superuser.
    """

    def has_permission(self, request, view):
        return (
            True
            if request.user.is_authenticated and request.user.is_superuser
            else False
        )
