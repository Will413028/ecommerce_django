from django.contrib import admin

# Register your models here.

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'brand', 'price']

    prepopulated_fields = {'slug': ('title',)}
