from django.shortcuts import render
from models import Product, Purchase, Order
from django.http import JsonResponse


def index(request):
    product_items = Product.objects.all()
    purchase_items = Purchase.objects.all()
    order_items = Order.objects.all()
    context = {
        'product_items': product_items,
        'purchase_items': purchase_items,
        'order_items': order_items
    }
    return render(request, 'index.html', context)


def display_product(request):
    product_items = Product.objects.all()
    context = {
        'product_items': product_items,
    }
    return render(request, 'product.html', context)


def display_purchase(request):
    purchase_items = Purchase.objects.all()
    context = {
        'purchase_items': purchase_items
    }
    return render(request, 'purchase.html', context)


def display_order(request):
    order_items = Order.objects.all()
    context = {
        'order_items': order_items
    }
    return render(request, 'order.html', context)


def display_report(request):
    labels = Product.objects.values_list('productlabel')
    productonhand = Product.objects.values_list('inventoryonhand')
    context = {
        'labels': labels,
        'productonhands': productonhand
    }
    return render(request, 'report.html', context)
