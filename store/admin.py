from django.contrib import admin
from django.http import HttpRequest
from .models import Category , Product , Auther , Order , OrderProduct , Slider
# Register your models here.




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_per_page = 20


@admin.register(Auther)
class AutherAdmin(admin.ModelAdmin):
    list_per_page = 20


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_per_page = 20


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_per_page = 20


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_per_page = 20

    def has_change_permission(self, request , ob=None):
        return False
    
    def has_add_permission(self, request):
        return False
    