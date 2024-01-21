# myapp/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Client, Product, Order


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'


