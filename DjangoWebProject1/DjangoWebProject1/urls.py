﻿"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Для магазина
from app.views import shop

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('links/', views.links, name='links'),
    path('feedback/', views.feedback, name='feedback'),
    path('blog/', views.blog, name='blog'),
    path('blogpost/<int:parametr>/', views.blogpost, name='blogpost'),
    path('newpost/', views.newpost, name="newpost"),
    path('videopost/', views.videopost, name='videopost'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Логин',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('registration/', views. registration, name='registration'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
