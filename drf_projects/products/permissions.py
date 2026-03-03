from rest_framework.permissions import SAFE_METHODS, BasePermission

from users.models import User


class IsVendorOwnerOrAdminReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return bool(request.user.is_authenticated)
        return bool(
            request.user.is_authenticated
            and request.user.role in {User.Role.ADMIN, User.Role.VENDOR}
        )

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return bool(request.user.is_authenticated)
        return bool(
            request.user.role == User.Role.ADMIN
            or (request.user.role == User.Role.VENDOR and obj.vendor_id == request.user.id)
        )
