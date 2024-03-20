"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.formsets import MIN_NUM_FORM_COUNT
from django.utils.translation import gettext_lazy as _
from .models import Feedback

from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class FeedbackForm(forms.Form):
    # Поле для ввода имени пользователя
    name = forms.CharField(label='Ваше имя', max_length=20, required=True)

    # Поле радио кнопок для выбора оценки сайта
    site_rating = forms.ChoiceField(
        label='Оцените сайт',
        choices=[
            ('1', 'Ужасно'),
            ('2', 'Плохо'),
            ('3', 'Средне'),
            ('4', 'Хорошо'),
            ('5', 'Отлично'),
        ],
        widget=forms.RadioSelect,
        required=True,
        initial=4
    )

    # Поле для ввода текстового отзыва
    feedback_text = forms.CharField(
        label='Ваш отзыв',
        widget=forms.Textarea(attrs={'rows': 4, 'style': 'resize: none;'}),
        required=True
    )

    # Флажки для указания предпочтений пользователя
    likes_merch = forms.BooleanField(label='Нравится мерч', required=False)
    likes_community = forms.BooleanField(label='Нравится сообщество', required=False)

    # Поле ввода текста
    favorite_game = forms.CharField(label='Ваша любимая игра', max_length=40, required=False)

    # Список для выбора опций из выпадающего списка
    suggestions = forms.ChoiceField(
        label='Ваши пожелания',
        choices=[
            ('Разнообразие мерча', 'Разнообразие мерча'),
            ('Добавление программы лояльности', 'Добавление программы лояльности'),
            ('Больше информативности', 'Больше информативности')
        ],
        widget=forms.Select,
        required=False
    )

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog # используемая модель
        fields = ('title', 'description', 'content', 'image',) # заполняемые поля
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}