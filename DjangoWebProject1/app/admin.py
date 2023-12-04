from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'category')
    search_fields = ('name', 'category__name')  # Добавим поиск по имени и категории

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']  # Список отображаемых полей в админке
