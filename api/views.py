from rest_framework import generics
from menu.models import Menu
from menu.serializers import MenuSerializer


# Create your views here.

class MenuListAPIView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer