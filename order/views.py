from rest_framework import generics
from .models import OrderItem
from serializers import OrderItemSerializer


# Create your views here.

class OrderItemListAPIView (generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer