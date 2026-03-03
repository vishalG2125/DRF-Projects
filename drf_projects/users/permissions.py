from rest_framework.permissions import BasePermission

from users.models import User


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role == User.Role.ADMIN)


class IsVendor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role == User.Role.VENDOR)


class IsVendorOwner(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role == User.Role.VENDOR)

    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_authenticated and obj.vendor_id == request.user.id)


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role == User.Role.CUSTOMER)
