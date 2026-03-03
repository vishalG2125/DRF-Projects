from django.db import transaction
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.permissions import IsAuthenticated

from orders.models import Order
from orders.serializers import OrderSerializer
from users.models import User
from users.permissions import IsAdminUser, IsCustomer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.select_related('customer', 'product').all()

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAdminUser()]
        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        user = self.request.user
        base_qs = self.queryset
        if user.role == User.Role.ADMIN:
            return base_qs
        if user.role == User.Role.CUSTOMER:
            return base_qs.filter(customer=user)
        if user.role == User.Role.VENDOR:
            return base_qs.filter(product__vendor=user)
        return base_qs.none()

    @transaction.atomic
    def perform_create(self, serializer):
        if self.request.user.role != User.Role.CUSTOMER:
            raise PermissionDenied('Only customers can place orders.')

        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']
        if product.stock < quantity:
            raise ValidationError('Insufficient stock for purchase.')

        product.stock -= quantity
        product.save(update_fields=['stock', 'updated_at'])
        serializer.save(customer=self.request.user)
