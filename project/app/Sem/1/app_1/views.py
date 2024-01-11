# from django.shortcuts import render
# Создайте представление “Привет, мир!” внутри вашего
# первого приложения.
# Настройте маршруты.

# Создайте новое приложение. Подключите его к проекту. В
# приложении должно быть три простых представления,
# возвращающих HTTP ответ:
# Орёл или решка
# Значение одной из шести граней игрального кубика
# Случайное число от 0 до 100
# Пропишите маршруты

import logging
from random import randint, choice
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):
    logger.info('index get request')
    return HttpResponse('Hello, world!')


def random_view(request):
    coin_sides = ['Heads', 'Tails']
    dice_side = randint(1, 6)
    rand_number = randint(0, 100)
    logger.info(f'Dice side: {dice_side}')
    logger.info(f'Random number from 0 to 100: {rand_number}')
    return HttpResponse(f'<p>Coin side: {choice(coin_sides)}</p><br><p>Dice side: {dice_side}</p>\
<br><p>Random number from 0 to 100: {rand_number}</p>')
