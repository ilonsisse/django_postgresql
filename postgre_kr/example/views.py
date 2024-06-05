from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Place, Shop
from .serializers import PlaceSerializer, ShopSerializer


class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer