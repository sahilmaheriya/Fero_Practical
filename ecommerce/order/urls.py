from django.urls import path
from .views import OrderListCreateView, OrdreUpdateView


urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='orders-list-create'),
    path('orders/<int:pk>/', OrdreUpdateView.as_view(), name='orders-update'),
]
