# Generated by Django 3.0.6 on 2020-05-18 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancies',
            old_name='vacancy_pulication_date',
            new_name='vacancy_publication_date',
        ),
    ]
