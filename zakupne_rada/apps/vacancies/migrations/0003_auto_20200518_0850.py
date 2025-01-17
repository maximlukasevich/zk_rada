# Generated by Django 3.0.6 on 2020-05-18 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_auto_20200518_0845'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancies',
            options={'verbose_name': 'Вакансію', 'verbose_name_plural': 'Вакансії'},
        ),
        migrations.AlterField(
            model_name='vacancies',
            name='vacancy_contact',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Контактна інформація для звернення'),
        ),
        migrations.AlterField(
            model_name='vacancies',
            name='vacancy_name',
            field=models.CharField(max_length=700, verbose_name='Назва вакансії'),
        ),
        migrations.AlterField(
            model_name='vacancies',
            name='vacancy_publication_date',
            field=models.DateTimeField(verbose_name='Дата публікації'),
        ),
        migrations.AlterField(
            model_name='vacancies',
            name='vacancy_salary',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Зарплата'),
        ),
    ]
