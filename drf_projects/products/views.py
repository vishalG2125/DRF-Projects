from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from products.permissions import IsVendorOwnerOrAdminReadOnly
from products.serializers import ProductSerializer
from users.models import User


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsVendorOwnerOrAdminReadOnly]
    queryset = Product.objects.select_related('vendor').all()
    filterset_fields = ['vendor', 'price']
    search_fields = ['name', 'description', 'vendor__username']
    ordering_fields = ['price', 'created_at', 'updated_at', 'name']

    def perform_create(self, serializer):
        if self.request.user.role == User.Role.ADMIN:
            serializer.save(vendor=self.request.user)
        else:
            serializer.save(vendor=self.request.user)
