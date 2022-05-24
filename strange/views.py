from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from strange.serializers import OrderSerializer, ItemSerializer
from strange.models import Order, Item
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view, action

# Create your views here.
def index(request):
    return HttpResponse("This is the Backend Index")

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint for orders
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id']

class ItemViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for items
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

@action(detail=False, methods=['POST'], name='Create orders')
def create_order(self, request):
    print(request.data)
    order_items_data = request.data.pop('order_items')

    buyer_id = request.data.pop('user')
    buyer = User.objects.get(pk=user_id)

    order = Order.objects.create(user=user, **request.data)
    for oi in order_items_data:
        name = oi.pop('name')
        id = oi.pop('id')
        product = item.objects.get(pk=id)
        order_item.objects.create(Order=order, item=product, **oi)
        ##returning an httpresponse
    return HttpResponse(order)