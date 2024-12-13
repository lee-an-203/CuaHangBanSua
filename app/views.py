from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import json


# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "app/home.html", context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(Customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_items": 0, "get_cart_total": 0}
    context = {"items": items, "order": order}
    return render(request, "app/cart.html", context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(Customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_items": 0, "get_cart_total": 0}
    context = {"items": items, "order": order}
    return render(request, "app/checkout.html", context)


def updateItem(request):
    data = json.loads(request.body)
    print("Received data:", data)  # In dữ liệu JSON nhận được

    productId = data.get('productId')
    action = data.get('action')
    print("Product ID:", productId, "Action:", action)

    customer = request.user.customer
    print("Customer:", customer)

    product = Product.objects.get(id=productId)
    print("Product:", product)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    print("Order:", order, "Created:", created)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    print("OrderItem:", orderItem, "Created:", created)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()
    print("OrderItem quantity after update:", orderItem.quantity)

    if orderItem.quantity <= 0:
        orderItem.delete()
        print("OrderItem deleted")

    return JsonResponse('added', safe=False)
