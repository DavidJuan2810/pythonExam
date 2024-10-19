from rest_framework.routers import DefaultRouter
from apps.orders.api.views import ProductViewSet, OrderViewSet, TableViewSet, ReservaViewSet

router1 = DefaultRouter()
router1.register(prefix='product', basename='product', viewset= ProductViewSet)
router1.register(prefix='order',basename='order', viewset=OrderViewSet)
router1.register(prefix='table', basename='table', viewset=TableViewSet)
router1.register(prefix='reserva', basename='reserva', viewset=ReservaViewSet)
