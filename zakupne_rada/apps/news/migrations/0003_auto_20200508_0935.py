# Generated by Django 3.0.6 on 2020-05-08 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200130_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_text',
            field=models.TextField(verbose_name='Текст новини'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_title',
            field=models.CharField(max_length=500, verbose_name='Заголовок новини'),
        ),
    ]