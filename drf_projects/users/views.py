from django.contrib.auth import get_user_model
from rest_framework import mixins, status, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.permissions import IsAdminUser
from users.serializers import (
    CustomerRegistrationSerializer,
    UserReadSerializer,
    VendorRegistrationSerializer,
)

User = get_user_model()


class CustomerRegistrationView(CreateAPIView):
    serializer_class = CustomerRegistrationSerializer
    permission_classes = []


class VendorRegistrationView(CreateAPIView):
    serializer_class = VendorRegistrationSerializer
    permission_classes = []


class AdminUserManagementViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = UserReadSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = User.objects.all().order_by('id')

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
