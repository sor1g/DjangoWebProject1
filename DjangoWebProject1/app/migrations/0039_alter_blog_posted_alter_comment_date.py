# Generated by Django 4.2.7 on 2023-12-03 02:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_alter_blog_posted_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 3, 5, 17, 4, 538740), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 3, 5, 17, 4, 538740), verbose_name='Дата комментария'),
        ),
    ]
