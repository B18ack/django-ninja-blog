# Generated by Django 5.1.7 on 2025-04-25 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0013_alter_articleimage_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleimage',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='blog_app.article', verbose_name='Статья'),
        ),
    ]
