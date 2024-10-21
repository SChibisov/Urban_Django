from django.http import *
from django.shortcuts import render


def flowers_shop(request):
    return render(request, "main.html")


def shop(request):
    header = 'Магазин цветов'
    button = 'Добавить в корзину'
    list_flowers = {'flower1': 'Гладиолус', 'flower2': 'Розы', 'flower3': 'Пионы'}
    data = {"header": header, "button": button, "products": list_flowers}
    return render(request, "shop.html", context=data)


def cart(request):
    return render(request, "shopping_cart.html")
