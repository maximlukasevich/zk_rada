from django.shortcuts import render
from .models import ReceptionSSchedules

def index(request):
    obj = ReceptionSSchedules.objects.all()
    return render(request, 'receptionSchedule/receptionSchedule.html', {'obj': obj})
