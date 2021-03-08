from django.shortcuts import render
from datetime import datetime


def main(request):
    content = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    content = {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    location = [
        {'city': 'Москва', 'phone': '+7-888-888-8888', 'email': 'info@geekshop.ru', 'address': 'В пределах МКАД'},
        {'city': 'Москва', 'phone': '+7-888-888-8888', 'email': 'info@geekshop.ru', 'address': 'В пределах МКАД'},
        {'city': 'Москва', 'phone': '+7-888-888-8888', 'email': 'info@geekshop.ru', 'address': 'В пределах МКАД'},
    ]
    content = {
        'title': 'Контакты',
        'location': location
    }
    return render(request, 'mainapp/contact.html', content)
