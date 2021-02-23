from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Vacancies

def index(request):
    vacancies_list = Vacancies.objects.order_by('-vacancy_publication_date')
    return render(request, 'vacancies/vacancies.html', {'vacancies_list': vacancies_list})