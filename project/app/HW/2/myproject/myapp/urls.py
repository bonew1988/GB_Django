# myapp/urls.py

from django.urls import path
from .views import (
    ClientListView, ClientDetailView,
    ProductListView, ProductDetailView,
    OrderListView, OrderDetailView,
)

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
]
