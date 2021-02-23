from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Contacts

def index(request):
    contacts = Contacts.objects.order_by('contact')
    return render(request, 'contacts/contacts.html', {'contacts': contacts})
