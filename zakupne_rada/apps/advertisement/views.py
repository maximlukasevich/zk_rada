from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Advertisements

def index(request):
    ad_list = Advertisements.objects.order_by('-ad_publication_date')
    return render(request, 'ad/ad_list.html', {'ad_list': ad_list})

def detail(request, ad_id):
    try:
        ad = Advertisements.objects.get( id = ad_id )
        return render(request, 'ad/detail.html', {'ad': ad})
    except:
        raise Http404
