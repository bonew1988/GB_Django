# populate_fake_data.py
import os
import django
from faker import Faker

# Установите переменную окружения DJANGO_SETTINGS_MODULE на ваш модуль настроек Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# Загрузите Django
django.setup()

# Теперь вы можете импортировать модели из вашего приложения
from myapp.models import Client, Product, Order
from django.utils import timezone

fake = Faker()

def create_clients(num_clients):
    for _ in range(num_clients):
        Client.objects.create(
            name=fake.name(),
            email=fake.email(),
            phone_number=fake.phone_number(),
            address=fake.address(),
            registration_date=fake.date_this_decade(),
        )

def create_products(num_products):
    for _ in range(num_products):
        Product.objects.create(
            name=fake.word(),
            description=fake.sentence(),
            price=fake.random_number(2),
            quantity=fake.random_int(min=1, max=100),
            added_date=fake.date_this_decade(),
        )

def create_orders(num_orders):
    clients = Client.objects.all()
    products = Product.objects.all()

    for _ in range(num_orders):
        order = Order.objects.create(
            client=fake.random_element(clients),
            total_amount=fake.random_number(3),
            order_date=fake.date_this_year(),
        )
        order.products.set(fake.random_elements(elements=products, length=fake.random_int(min=1, max=5)))

if __name__ == "__main__":
    num_clients = 100
    num_products = 2000
    num_orders = 400

    create_clients(num_clients)
    create_products(num_products)
    create_orders(num_orders)

    print("Fake data has been populated.")
