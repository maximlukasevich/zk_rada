# Generated by Django 3.0.6 on 2020-05-18 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0003_auto_20200518_0850'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancies',
            options={'verbose_name': 'Вакансія', 'verbose_name_plural': 'Вакансії'},
        ),
        migrations.AlterField(
            model_name='vacancies',
            name='vacancy_contact',
            field=models.CharField(max_length=500, verbose_name='Контактна інформація для звернення'),
        ),
    ]
