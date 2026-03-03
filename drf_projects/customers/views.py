from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from orders.models import Order
from orders.serializers import OrderSerializer
from users.permissions import IsCustomer


class CustomerOrderViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsCustomer]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).select_related('product', 'customer')
