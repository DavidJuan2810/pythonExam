from rest_framework.serializers import ModelSerializer
from apps.orders.models import Product,Order, Table, Reservation

# Creation of the serializer model of product model
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
# Creation of the serializer model of order model
class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
# Creation of the serializer model of table model
class TableSerializer(ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

# Creation of serializer of the reservation model
class ReservaSerializer(ModelSerializer):
    class Meta:
        model = Reservation 
        fields = '__all__'