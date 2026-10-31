from django.contrib import admin
from .models import Establishment, Kitchen, Category, Food, Address, Order

@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'delivery_time', 'delivery_price_from', 'address')
    search_fields = ('name', 'address')


@admin.register(Kitchen)
class KitchenAdmin(admin.ModelAdmin):
    list_display = ('id', 'establishment', 'name')
    list_filter = ('establishment',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'kitchen', 'name')
    list_filter = ('kitchen',)
    search_fields = ('name',)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'kitchen',)
    list_filter = ('kitchen', )
    search_fields = ('name',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'name', 'address', 'is_default')
    search_fields = ('name', 'address')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('id', 'user__email')