from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from .models import (
    Product, Order, OrderItem, VarietySpec, Address)

class AddressAdmin(admin.ModelAdmin):
    list_display=[
        'user',
        'address_type',
        'address_line_1',
        'address_line_2',
        'county',
        'eircode',
    ]

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(VarietySpec)
admin.site.register(Address, AddressAdmin)

