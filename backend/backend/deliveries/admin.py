from django.contrib import admin
from .models import (
    PaymentMethod,
    DeliveryFee,
    Delivery
)


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    list_filter = [
        'name',
    ]


@admin.register(DeliveryFee)
class DeliveryFeeAdmin(admin.ModelAdmin):
    list_display = [
        'price',
    ]


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = [
        'date',
        'motoboy_id',
        'price',
        'status',
        'delivery_fee_id',
        'payment_method_id'
    ]
    list_filter = [
        'date',
        'motoboy_id',
        'status',
        'delivery_fee_id',
        'payment_method_id'
    ]
