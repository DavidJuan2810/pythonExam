from rest_framework.routers import DefaultRouter
from apps.orders.api.views import ProductViewSet, OrderViewSet

router1 = DefaultRouter()
router1.register(prefix='product', basename='product', viewset= ProductViewSet)
router1.register(prefix='order',basename='order', viewset=OrderViewSet)
