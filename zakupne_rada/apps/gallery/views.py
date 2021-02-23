from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Photos

def index(request):
    slider = Photos.objects.order_by('-photo_publication_date')[:5]
    gallery = Photos.objects.order_by('-photo_publication_date')
    return render(request, 'gallery/gallery.html', {'gallery': gallery, 'slider': slider})