from django.contrib import admin
from apps.orders.models import Product,Order
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)