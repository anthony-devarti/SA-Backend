from django.contrib.auth.models import User, Group
from strange.models import Order, Item
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields ='__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'