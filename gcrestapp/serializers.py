from rest_framework import serializers

from .models import Restaurant, Delivery

class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    delivery = DeliverySerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Restaurant
        fields = '__all__'
