# myapp/urls.py

from django.urls import path
from .views import (
    ClientListView, ClientDetailView,
    ProductListView, ProductDetailView,
    OrderListView, OrderDetailView,
    client_ordered_products,  # Import the new view
)

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/<int:client_id>/ordered-products/', client_ordered_products, name='client_ordered_products'),  # Add this line
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
]
