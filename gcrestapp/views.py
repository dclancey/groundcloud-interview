from rest_framework import generics, status, viewsets

from .models import Restaurant,Delivery
from .serializers import RestaurantSerializer,DeliverySerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
