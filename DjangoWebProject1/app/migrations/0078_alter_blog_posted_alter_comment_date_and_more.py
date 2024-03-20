# Generated by Django 4.2.7 on 2023-12-08 16:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0077_product_sizes_alter_blog_posted_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 8, 19, 3, 17, 718372), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 8, 19, 3, 17, 719370), verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Размер товара'),
        ),
    ]