from rest_framework import viewsets

from system.models import Product
from system.models.product import SeasonalProduct, BulkProduct, PremiumProduct
from system.serializers.product_serializer import ProductSerializer, SeasonalProductSerializer, BulkProductSerializer, \
    PremiumProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSerializer
        elif self.action == 'create' or self.action == 'update':
            return ProductSerializer

class SeasonalProductViewSet(ProductViewSet):
    queryset = SeasonalProduct.objects.all()
    serializer_class = SeasonalProductSerializer

class BulkProductViewSet(ProductViewSet):
    queryset = BulkProduct.objects.all()
    serializer_class = BulkProductSerializer

class PremiumProductViewSet(ProductViewSet):
    queryset = PremiumProduct.objects.all()
    serializer_class = PremiumProductSerializer