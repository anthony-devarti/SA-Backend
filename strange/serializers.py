from django.contrib.auth.models import User, Group
from strange.models import Order, Item
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'total_paid', 
            'pub_date', 
            'suggested', 
            'delta', 
            'seller', 
            'note', 
            'buyer', 
            'method',
            'item_set'
            ]
        depth = 1


class ItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    class Meta:
        model = Item
        fields = [
            'id',
            'name',
            'set_name',
            'order'
        ]
        depth = 1
