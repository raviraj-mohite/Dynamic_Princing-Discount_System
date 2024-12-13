from django.urls import path, include
from rest_framework.routers import DefaultRouter

from system.viewsets.Discount_viewset import DiscountViewSet
from system.viewsets.order_viewset import OrderViewSet
from system.viewsets.product_viewset import ProductViewSet, SeasonalProductViewSet, BulkProductViewSet, \
    PremiumProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'products/seasonal', SeasonalProductViewSet, basename='seasonal-product')
router.register(r'products/bulk', BulkProductViewSet, basename='bulk-product')
router.register(r'products/premium', PremiumProductViewSet, basename='premium-product')
router.register(r'discounts', DiscountViewSet, basename='discount')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
