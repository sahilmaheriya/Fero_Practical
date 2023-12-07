from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'weight']
        
    def validate_weight(self, value):
        if value < 0 or value > 25:
            raise serializers.ValidationError("Weight must be positive and not more than 25kg")
        return value