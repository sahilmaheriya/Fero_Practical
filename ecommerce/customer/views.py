from rest_framework.generics import UpdateAPIView, ListCreateAPIView
from rest_framework.response import Response
from .serializer import CustomerSerializer
from .models import Customer



class CustomersListCreateView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

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
            "message": "Customer created successfully.",
            "data": response.data
        }
        return Response(data)


class CustomerUpdateView(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
    def put(self, request, *args, **kwargs):
        response = self.partial_update(request, *args, **kwargs)
        data = {
            "status":response.status_code,
            "message": "Customer updated successfully.",
            "data": response.data
        }
        return Response(data)