# Generated by Django 5.1.6 on 2025-02-25 12:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_category_alter_faq_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('slug', models.SlugField(verbose_name='Слаг')),
                ('short_description', models.TextField(verbose_name='Краткое описание')),
                ('full_description', models.TextField(blank=True, null=True, verbose_name='Полное описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='articles/previews/', verbose_name='Превью')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='blog_app.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
