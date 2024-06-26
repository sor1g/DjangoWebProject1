# Generated by Django 4.2.7 on 2023-12-09 17:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0091_alter_blog_posted_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 9, 20, 48, 36, 574605), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 9, 20, 48, 36, 574605), verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='favorite_game',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='likes_community',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='likes_merch',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='site_rating',
            field=models.CharField(choices=[('1', 'Ужасно'), ('2', 'Плохо'), ('3', 'Средне'), ('4', 'Хорошо'), ('5', 'Отлично')], max_length=1),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='suggestions',
            field=models.CharField(blank=True, choices=[('Разнообразие мерча', 'Разнообразие мерча'), ('Добавление программы лояльности', 'Добавление программы лояльности'), ('Больше информативности', 'Больше информативности')], max_length=50, null=True),
        ),
    ]
