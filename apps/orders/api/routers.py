from rest_framework.routers import DefaultRouter
from apps.orders.api.views import ProductViewSet, OrderViewSet, TableViewSet, ReservaViewSet

router2 = DefaultRouter()
router2.register(prefix='product', basename='product', viewset= ProductViewSet)
router2.register(prefix='order',basename='order', viewset=OrderViewSet)
router2.register(prefix='table', basename='table', viewset=TableViewSet)
router2.register(prefix='reserva', basename='reserva', viewset=ReservaViewSet)

