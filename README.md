# Dynamic Pricing and Discount System
This project is a Django-based system for managing products, discounts, and orders. It demonstrates the use of Django models, serializers, and viewsets to implement a flexible pricing and discounting mechanism.

## Features

- **Products**: Includes base products and specialized product types such as seasonal, bulk, and premium products with customized pricing logic.
- **Discounts**: Multiple discount types, including percentage, fixed amount, and tiered discounts.
- **Orders**: Support for calculating the total price of orders by applying applicable discounts.

## Directory Structure

```plaintext
pricing_discount/
├── pricing_discount/         # Django project settings and configuration
├── system/                   # App containing models, serializers, views, and URLs
│   ├── models/               # Model definitions for Product, Discount, and Order
│   ├── serializers/          # Serializer definitions for Product, Discount, and Order
│   ├── views/                # ViewSets for Product, Discount, and Order
│   └── urls.py               # URLs for system app
└── manage.py                 # Django management script
