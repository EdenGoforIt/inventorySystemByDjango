from django.contrib import admin
from models import Order, Purchase, Supplier, Product



@admin.register(Order, Purchase, Supplier, Product)
class ViewAdmin(admin.ModelAdmin):
    pass
