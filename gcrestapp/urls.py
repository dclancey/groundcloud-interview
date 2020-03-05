from django.conf.urls import url,include, re_path
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet,DeliveryViewSet

router = DefaultRouter()

router.register(r'restaurants', RestaurantViewSet,basename='restaurants')
router.register(r'deliveries', DeliveryViewSet,basename='deliveries')

urlpatterns = [
    re_path('^', include(router.urls)),
]