# This is a controller

from django.shortcuts import render

# Create your views here.


def all(request):
    return render(request, 'online_shop_app/pages/all.html')

def category1(request):
    return render(request, 'online_shop_app/pages/category1.html')

def category2(request):
    return render(request, 'online_shop_app/pages/category2.html')

def category3(request):
    return render(request, 'online_shop_app/pages/category3.html')

def signIn(request):
    return render(request, 'online_shop_app/pages/signIn.html')

def signUp(request):
    return render(request, 'online_shop_app/pages/signUp.html')

def cart(request):
    return render(request, 'online_shop_app/pages/cart.html')