from django.contrib import admin
from models import Order, Purchase, Supplier, Product, Alert



@admin.register(Order, Purchase, Supplier, Product, Alert)
class ViewAdmin(admin.ModelAdmin):
    pass
