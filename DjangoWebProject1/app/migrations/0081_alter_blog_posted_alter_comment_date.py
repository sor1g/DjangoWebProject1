# Generated by Django 4.2.7 on 2023-12-08 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0080_cart_alter_blog_posted_alter_comment_date_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 8, 19, 53, 55, 374494), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 8, 19, 53, 55, 374494), verbose_name='Дата комментария'),
        ),
    ]
