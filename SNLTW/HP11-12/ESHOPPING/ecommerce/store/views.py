from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product, Cart, Customer, Cartitems
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
import requests

def store(request):
    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
    #     cartitems = cart.cartitems_set.all()
    products = Product.objects.all() 
    # paginator = Paginator(products, 3)
    # pageNumber = request.GET.get('page')
    # try:
    #     products = paginator.page(pageNumber)
    # except PageNotAnInteger:
    #     products = paginator.page(1)
    # except EmptyPage:
    #     products = paginator.page(paginator.num_pages)
    return render(request, 'pages/store.html', {'products':products, 'cart':cart})

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}
    return render(request, 'pages/cart.html', {'cartitems' : cartitems, 'cart':cart})

def updateCart(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    product = Product.objects.get(id=productId)
    customer = request.user.customer
    cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
    cartitem, created = Cartitems.objects.get_or_create(cart = cart, product = product)
    if action == "add":
        cartitem.quantity += 1
        cartitem.save()
    return JsonResponse("Cart Updated", safe = False)

def checkout(request):
    return render(request, 'pages/checkout.html',{})