from django.db import models

from system.models import Product, Discount


class Order(models.Model):
    products = models.ManyToManyField(Product)
    discounts = models.ManyToManyField(Discount)

    def calculate_total(self):
        total = sum([product.get_price(quantity=1) for product in self.products.all()])
        for discount in self.discounts.all():
            total = discount.apply_discount(total)
        return total