from django.contrib import admin
from .models import Product, Client, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number',
                    'address', 'registration_date')
    search_fields = ('name', 'email', 'phone_number')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'added_date')
    search_fields = ('name', 'price', 'quantity')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total_amount', 'order_date')
    search_fields = ('client__name', 'total_amount', 'order_date')

    filter_horizontal = ('products',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
