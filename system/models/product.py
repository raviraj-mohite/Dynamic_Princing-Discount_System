from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    base_price = models.FloatField()

    def get_price(self, quantity=1):
        return self.base_price

class SeasonalProduct(Product):
    def get_price(self, quantity=1):
        # Assume 20% discount for winter season
        discount = 0.2
        return self.base_price * (1 - discount)

class BulkProduct(Product):
    def get_price(self, quantity=1):
        # Tiered discounts based on quantity
        if quantity >= 10 and quantity <= 20:
            discount = 0.05  # 5% off
        elif quantity >= 21 and quantity <= 50:
            discount = 0.10  # 10% off
        elif quantity > 50:
            discount = 0.15  # 15% off
        else:
            discount = 0
        return self.base_price * quantity * (1 - discount)

class PremiumProduct(Product):
    def get_price(self, quantity=1):
        markup = 0.15  # 15% markup for premium features
        return self.base_price * (1 + markup)

