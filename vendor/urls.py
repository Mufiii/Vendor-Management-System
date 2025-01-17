from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet , PurchaseOrderViewSet

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchase-orders', PurchaseOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

