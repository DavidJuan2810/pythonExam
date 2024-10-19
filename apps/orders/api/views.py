from rest_framework.viewsets import ModelViewSet
from apps.orders.models import Product, Order,Table, Reservation
from apps.orders.serializers import ProductSerializer, OrderSerializer,TableSerializer, ReservaSerializer

# Model ViewSet of the product model
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Model ViewSet of the order model
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Model ViewSet of the table model
class TableViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    
# Model ViewSet of the reservation model
class ReservaViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservaSerializer