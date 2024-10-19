from django.contrib import admin
from apps.orders.models import Product,Order, Table, Reservation
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Table)
admin.site.register(Reservation)