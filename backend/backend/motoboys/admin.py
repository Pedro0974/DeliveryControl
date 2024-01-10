from django.contrib import admin
from .models import Motoboy


@admin.register(Motoboy)
class MotoboyAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'age',
        'phone'
    ]
    list_filter = [
        'name',
    ]
