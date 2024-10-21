from django.http import *
from django.shortcuts import render


def flowers_shop(request):
    return render(request, "main.html")


def shop(request):
    header = 'Магазин цветов'
    button = 'Добавить в корзину'
    flowers = ['Гладиолус', 'Розы', 'Пионы']
    data = {"header": header, "button": button, "flowers": flowers}
    return render(request, "shop.html", context=data)


def cart(request):
    return render(request, "shopping_cart.html")
