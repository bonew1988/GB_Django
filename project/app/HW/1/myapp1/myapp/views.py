import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)

def home(request):
    logger.info(f"Пользователь посетил главную страницу: {request.META['REMOTE_ADDR']}")
    return render(request, 'myapp/home.html')

def about(request):
    logger.info(f"Пользователь посетил страницу 'О себе': {request.META['REMOTE_ADDR']}")
    return render(request, 'myapp/about.html')
