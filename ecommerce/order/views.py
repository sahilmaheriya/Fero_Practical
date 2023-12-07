from .models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order_items__product__name', 'customer__name']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        product_name = self.request.query_params.get('product', None)
        customer_name = self.request.query_params.get('customer', None)
        if customer_name:
            queryset = queryset.filter(customer__name=customer_name)
        if product_name:
            product_name = product_name.split(',')
            queryset = queryset.filter(order_items__product__name__in=product_name)
        return queryset

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        data = {
            "status": response.status_code,
            "data": response.data,
        }
        return Response(data)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = {
            "status": response.status_code,
            "message": "Product created successfully.",
            "data": response.data
        }
        return Response(data)


class OrdreUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def put(self, request, *args, **kwargs):
        response = self.partial_update(request, *args, **kwargs)
        data = {
            "status":response.status_code,
            "message": "Customer updated successfully.",
            "data": response.data
        }
        return Response(data)