from django.shortcuts import render
from django.http import Http404, HttpResponse, QueryDict
from .models import Appeals
from django.utils import timezone
import datetime

def index(request):
    return render(request, 'appeal/appeal.html')

def thanks(request):
    if request.method == "POST":
        mail = request.POST['mail']
        if (request.POST['message'] != ""):
            message = request.POST['message']
            date = timezone.datetime.now()
            new_appeal = Appeals.objects.create(appeal_mail = mail, appeal_message = message, appeal_status = False, appeal_date = date )
            new_appeal.save()
            return render(request, 'appeal/thanks.html')
        else:
            return render(request, 'appeal/appeal.html')