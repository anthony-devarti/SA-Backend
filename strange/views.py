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
    filterset_fields = ['id', 'buyer__id']

class ItemViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for items
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    ##This is what the order object will look like from the frontend
    # const orderObject = {
    #   "total_paid": total,
    #   "pub_date": "now",
    #   "suggested": suggested,
    #   "delta": difference,
    #   "seller": "Unknown",
    #   "note": "None",
    #   "buyer": userid (hard code this as 1 for now)
    #   order_items: cart,
    #   method: method (hard code this as 1 for now)
    # }
    ## This is what it looked like originally
    #   const orderObject = {
    #     total: total,
    #     paid: true,
    #     user: state.currentUser.user_id,
    #     order_items: cart,
    #}
    
    @action(detail=False, methods=['POST'], name='Create orders')
    def create_orders(self, request):
        print(request.data)
        #this all matches and lines up with the info above
        order_items_data = request.data.pop('order_items')

        #changed user to buyer
        user_id = request.data.pop('buyer')
        buyer = User.objects.get(pk=user_id)

        order = Order.objects.create(buyer=buyer, **request.data)
        for oi in order_items_data:
            name = oi.pop('name')
            condition = oi.pop('condition')
            estimate = oi.pop('Estimate')
            actual = oi.pop('Actual')
            Item.objects.create(order=order, name=name, condition=condition, **oi)
            ##returning an httpresponse
        return HttpResponse(order)