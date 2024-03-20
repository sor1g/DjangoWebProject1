"""
Definition of models.
"""

from ctypes.wintypes import SIZE
from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render


# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    site_rating = models.CharField(max_length=1, choices=[
        ('1', 'Ужасно'),
        ('2', 'Плохо'),
        ('3', 'Средне'),
        ('4', 'Хорошо'),
        ('5', 'Отлично'),
    ], verbose_name='Оценка сайта')
    feedback_text = models.TextField(verbose_name='Отзыв')
    likes_merch = models.BooleanField(verbose_name='Нравится мерч')
    likes_community = models.BooleanField(verbose_name='Нравится сообщество')
    favorite_game = models.CharField(max_length=40, blank=True, null=True, verbose_name='Любимая игра')
    suggestions = models.CharField(max_length=50, choices=[
        ('Разнообразие мерча', 'Разнообразие мерча'),
        ('Добавление программы лояльности', 'Добавление программы лояльности'),
        ('Больше информативности', 'Больше информативности')
    ], blank=True, null=True, verbose_name='Пожелания')

    def __str__(self):
        return self.name
   
    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"


# Модель данных Блога
class Blog(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголовок")
    description = models.TextField(verbose_name = "Краткое содержание")
    content = models.TextField(verbose_name = "Полное содержание")
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image = models.FileField(default = 'temp.jpg', verbose_name = "Путь к картинке")

    # Методы класса:
    def get_absolute_url(self): # метод возвращает строку с URL-адресом записи
        return reverse("blogpost", args=[str(self.id)])

    def __str__(self): # метод возвращает название, используемое для представления отдельных записей в административном разделе
        return self.title

    # Метаданные – вложенный класс, который задает дополнительные параметры модели:
    class Meta:
        db_table = "Posts" # имя таблицы для модели
        ordering = ["-posted"] # порядок сортировки данных в модели ("-" означает по убыванию)
        verbose_name = "статья блога" # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)
        verbose_name_plural = "статьи блога" # тоже для всех статей блога

admin.site.register(Blog)

class Comment(models.Model):
    text = models.TextField(verbose_name = "Текст комментария")
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата комментария")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор комментария")
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Статья комментария")
    
    # Методы класса:
    def __str__(self): # метод возвращает название, используемое для представления отдельных записей в административном разделе
        return 'Комментарий %d %s к %s' % (self.id, self.author, self.post)
    
    # Метаданные - вложенный класс, который задает дополнительные параметры модели:
    class Meta:
        db_table = "Comment"
        ordering = ["-date"]
        verbose_name = "Комментарий к статье блога"
        verbose_name_plural = "Комментарии к статьям блога"
        
admin.site.register(Comment)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория товара"
        verbose_name_plural = "категории товаров"

    
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название товара", default="Default Name")
    description = models.TextField(verbose_name="Описание товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория товара")
    image = models.CharField(max_length=255, verbose_name="Путь к изображению товара")
    image_2 = models.CharField(max_length=255, null=True, blank=True, verbose_name="Путь ко второму изображению")
    sizes = models.CharField(max_length=20, blank=True, null=True, verbose_name="Размер товара")
  
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('В обработке', 'В обработке'),], default='В обработке')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказ {self.id}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Элемент заказа {self.id}"

    class Meta:
        verbose_name = "Элемент заказа"
        verbose_name_plural = "Элементы заказа"
