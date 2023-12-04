"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest

from app.forms import FeedbackForm
from .forms import BlogForm, FeedbackForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.db import models
from .models import Blog

from .models import Comment # использование модели комментариев
from .forms import CommentForm # использование формы ввода комментария

# Для магазина
from django.shortcuts import render
from .models import Category, Product

def home(request):
    """Отображать the home страницу."""
    assert isinstance(request, HttpRequest)
    
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def shop(request):
    """Отображать the shop страницу."""
    categories = Category.objects.all()
    selected_category = None
    products = Product.objects.all()
    category_id = request.GET.get('category_id')
    
    if category_id:
        selected_category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=selected_category)
        
    return render(
        request,
       'app/shop.html',
      {
          'title': 'Магазин', 
          'categories': categories,
          'selected_category': selected_category,
          'products': products,
          'year':datetime.now().year,
      }
    )

def category(request, category_id):
    """Отображать the category страницу."""
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    return render(
        request, 
        'app/category.html', 
        {   
            'title': 'Категории',
            'categories': Category.objects.all(),
            'products': products,
            'year':datetime.now().year,
        }
    )

def product_detail(request, product_id):
    """Отображать the category страницу."""
    product = get_object_or_404(Product, id=product_id)
    return render(
        request, 
        'app/product_detail.html', 
        {
        'title': ' ',
        'product': product,
        'year':datetime.now().year,
        }
    )

def about(request):
    """Отображать the about страницу."""
    assert isinstance(request, HttpRequest)
    
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Сведения о нас.',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Отображать the contact страницу."""
    assert isinstance(request, HttpRequest)
    
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Страница с нашими контактами.',
            'year':datetime.now().year,
        }
    )

def links(request):
    """Отображать the links страницу."""
    assert isinstance(request, HttpRequest)
    
    return render(
        request,
        'app/links.html',
        {
            'title':'Полезные ресурсы',
            'message':'Ссылки.',
            'year':datetime.now().year,
        }
    )

def feedback(request):
    """Отображать the feedback страницу."""
    assert isinstance(request, HttpRequest)
    data = None
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Код, который выполняется, если форма прошла валидацию
            data = dict()
            data ['name'] = form.cleaned_data['name']
            data ['site_rating'] = form.cleaned_data['site_rating']
            data ['feedback_text'] = form.cleaned_data['feedback_text']
            if (form.cleaned_data['likes_merch'] == True):
                data ['likes_merch'] = 'Да'
            else:
                data ['likes_merch'] = 'Нет'
            if (form.cleaned_data['likes_community'] == True):
                data ['likes_community'] = 'Да'
            else:
                data ['likes_community'] = 'Нет'
            data ['favorite_game'] = form.cleaned_data['favorite_game']
            data ['suggestions'] = form.cleaned_data['suggestions']
            form = None
    else:
        form = FeedbackForm()
        
    return render(
        request,
        'app/feedback.html',
        {
            'title':'Обратная связь',
            'form':form,
            'data':data
        }
    )

def blog(request):
    """Отображать the blog страницу."""
    assert isinstance(request, HttpRequest)
    posts = Blog.objects.all() # запрос на выбор всех статей блога из модели
    
    return render(
        request,
        'app/blog.html',
        {
        'title':'Блог',
        'posts':posts, # передача списка статей в шаблон веб-страницы
        'year':datetime.now().year,
        }
    )

def blogpost(request, parametr):
    """Отображать the blogpost страницу."""
    assert isinstance(request, HttpRequest)
    post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(post=parametr)
    
    if request.method == "POST": # после отправки данных формы на сервер методом POST
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя
            comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату
            comment_f.post = Blog.objects.get(id=parametr) # добавляем в модель Комментария (Comment) статью, для которой данный комментарий
            comment_f.save() # сохраняем изменения после добавления полей
            return redirect('blogpost', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки комментария
    else:
        form = CommentForm() # создание формы для ввода комментария

    return render(
        request,
        'app/blogpost.html',
        {
        'title':post_1,
        'post_1':post_1, # передача конкретной статьи в шаблон веб-страницы
        'comments':comments, # передача всех комментариев к данной статье в шаблон веб-страницы
        'form':form, # передача формы добавления комментария в шаблон веб-страницы
        'year':datetime.now().year,
        }
    )

def newpost(request):
    """Отображать the newpost страницу."""
    assert isinstance(request, HttpRequest)
    
    if request.method == "POST": # после отправки формы
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.autor = request.user
            blog_f.save() # сохраняем изменения после добавления полей
            return redirect('blog') # переадресация на страницу Блог после создания статьи Блога
    else:
        blogform = BlogForm() # создание объекта формы для ввода данных
        
    return render(
        request,
        'app/newpost.html',
        {
        'title': 'Добавить статью блога',
        'blogform':blogform, # передача формы в шаблон веб-страницы
        'year':datetime.now().year,
        }
    )
    
def videopost(request):
    """Отображать the vedeopost cтраницу."""
    assert isinstance(request, HttpRequest)
    
    return render(
        request,
        'app/videopost.html',
        {
            'title':'Видео',
            'year':datetime.now().year,
        }
    )

def registration(request):
    """Отображать the registration страницу."""
    assert isinstance(request, HttpRequest)
    
    if request.method == "POST": # после отправки формы
        regform = UserCreationForm (request.POST)
        if regform.is_valid(): #валидация полей формы
            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы
            reg_f.is_staff = False # запрещен вход в административный раздел
            reg_f.is_active = True # активный пользователь
            reg_f.is_superuser = False # не является суперпользователем
            reg_f.date_joined = datetime.now() # дата регистрации
            reg_f.last_login = datetime.now() # дата последней авторизации
            reg_f.save() # сохраняем изменения после добавления данных
        return redirect('home') # переадресация на главную страницу после регистрации
    else:
        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя
        
    return render(
        request,
        'app/registration.html',
        {
        'title':'Регистрация',
        'regform': regform, # передача формы в шаблон веб-страницы
        'year':datetime.now().year,
        }
    )