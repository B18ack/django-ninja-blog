# Generated by Django 5.1.6 on 2025-02-18 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_faq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Вопрос'),
        ),
    ]
