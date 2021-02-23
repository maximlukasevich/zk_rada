from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Deputies

def index(request):
    deputies_list = Deputies.objects.all()
    return render(request, 'deputies/deputies.html', {'deputies_list': deputies_list})
