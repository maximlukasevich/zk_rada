# Generated by Django 3.0.6 on 2020-06-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeals',
            name='appeal_mail',
            field=models.TextField(verbose_name='Електронна пошта'),
        ),
    ]
