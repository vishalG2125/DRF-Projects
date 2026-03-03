from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from customers.views import CustomerOrderViewSet
from orders.views import OrderViewSet
from products.views import ProductViewSet
from users.views import AdminUserManagementViewSet, CustomerRegistrationView, VendorRegistrationView
from vendors.views import VendorProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'admin/users', AdminUserManagementViewSet, basename='admin-users')
router.register(r'vendor/products', VendorProductViewSet, basename='vendor-products')
router.register(r'customer/orders', CustomerOrderViewSet, basename='customer-orders')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/customer/', CustomerRegistrationView.as_view(), name='customer-register'),
    path('api/auth/register/vendor/', VendorRegistrationView.as_view(), name='vendor-register'),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]
