from django.urls import path, include
from .views import CustomerUpdateView, CustomersListCreateView


urlpatterns = [
    path('customers/', CustomersListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerUpdateView.as_view(), name='customer-udpate'),
]
