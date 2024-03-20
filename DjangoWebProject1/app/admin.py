from django.contrib import admin
from .models import Category, Product
from .models import Feedback

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'sizes', 'category')
    search_fields = ('name', 'category__name')  # Добавим поиск по имени и категории
    ordering = ('id',)  # Сортировка по умолчанию по полю 'id'
    list_display_links = ('id', 'name')  # Устанавливаем гиперссылку для поля 'name'

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']  # Список отображаемых полей в админке

admin.site.register(Feedback) # Регистрируем модель Feedback