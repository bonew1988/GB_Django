from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.utils import timezone
from datetime import timedelta
from .models import Client, Product, Order
from .forms import ProductForm


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Calculate the date thresholds
        today = timezone.now().date()
        one_week_ago = today - timedelta(days=7)
        one_month_ago = today - timedelta(days=30)
        one_year_ago = today - timedelta(days=365)

        # Get unique products ordered by the client within the specified time intervals
        context['products_last_week'] = Product.objects.filter(
            order__client=self.object, order__order_date__gte=one_week_ago).distinct()
        context['products_last_month'] = Product.objects.filter(
            order__client=self.object, order__order_date__gte=one_month_ago).distinct()
        context['products_last_year'] = Product.objects.filter(
            order__client=self.object, order__order_date__gte=one_year_ago).distinct()

        return context


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


def client_ordered_products(request, client_id):
    client = Client.objects.get(pk=client_id)

    # Calculate the date thresholds
    today = timezone.now().date()
    one_week_ago = today - timedelta(days=7)
    one_month_ago = today - timedelta(days=30)
    one_year_ago = today - timedelta(days=365)

    # Get unique products ordered by the client within the specified time intervals
    products_last_week = Product.objects.filter(
        order__client=client, order__order_date__gte=one_week_ago).distinct()
    products_last_month = Product.objects.filter(
        order__client=client, order__order_date__gte=one_month_ago).distinct()
    products_last_year = Product.objects.filter(
        order__client=client, order__order_date__gte=one_year_ago).distinct()

    context = {
        'client': client,
        'products_last_week': products_last_week,
        'products_last_month': products_last_month,
        'products_last_year': products_last_year,
    }

    return render(request, 'client_ordered_products.html', context)

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Перенаправление после успешного сохранения
    else:
        form = ProductForm()

    return render(request, 'product_create.html', {'form': form})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()

    else:
        form = ProductForm(instance=product)

    return render(request, 'myapp/product_detail.html', {'product': product, 'form': form})


