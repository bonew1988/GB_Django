from django.urls import path
from myapp.views import home, about

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
]
