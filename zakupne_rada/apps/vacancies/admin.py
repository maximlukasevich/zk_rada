from django.contrib import admin
from .models import Vacancies

class AdminPanel(admin.ModelAdmin):
    list_display = ('vacancy_name', 'vacancy_number', 'vacancy_criterion', 'vacancy_contact', 'vacancy_publication_date')

admin.site.register(Vacancies, AdminPanel)
