from rest_framework import serializers
from .models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['created_at', 'updated_at', 'name', 'tax', 'total', 'isCompleted', 'order']