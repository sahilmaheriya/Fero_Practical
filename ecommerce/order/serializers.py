from datetime import date
from rest_framework import serializers
from .models import Order, OrderItem
from product.serializers import ProductSerializer
from customer.serializer import CustomerSerializer



class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        product = ProductSerializer(instance.product).data
        response['product'] = product
        return response


class OrderSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer(many=True, required=False)
    order_date = serializers.DateField(input_formats=["%d/%m/%Y"])
    class Meta:
        model = Order
        fields = ['id', 'order_number', 'customer', 'order_date', 'address', 'order_item']
    
    def validate_order_date(self, order_date):
        if order_date <= date.today():
            raise serializers.ValidationError('Order Date cannot be in past.')
        else:          
            return order_date
    
    def validate(self, attrs):
        cumlative_weight = 0
        for item in attrs['order_item']:
            cumlative_weight+=item['product'].weight * item['quantity']
        if cumlative_weight > 150:
            raise serializers.ValidationError('Order cumulative weight must be under 150')
        return super().validate(attrs)
    
    def create(self, validated_data):
        order_items = validated_data.pop('order_item')
        response = super().create(validated_data)
        for items in order_items:
            OrderItem.objects.create(order=response, **items)
        return response
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        order_items = instance.order_items.all()
        serializer = OrderItemSerializer(order_items, many=True).data
        response['order_items'] = serializer
        response['customer'] = CustomerSerializer(instance.customer).data
        return response