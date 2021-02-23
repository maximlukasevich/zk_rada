from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Cards
from news.models import News
from advertisement.models import Advertisements
from documents.models import Documents
from django.db.models.functions import Lower
from django.utils import timezone
import datetime


def index(request):
    last_documents = Documents.objects.order_by('-documents_publication_date')[:3]
    category = []
    for get_category in last_documents:
        category += Documents.objects.filter( category__category_name = get_category.category )
        
    last_news = News.objects.order_by('-news_publication_date')[:3]
    last_ad= Advertisements.objects.order_by('-ad_publication_date')[:3]
    cards = Cards.objects.order_by('id')
    data = {'last_news': last_news, 'last_ad': last_ad, 'cards': cards, 'last_documents': last_documents, 'category': category}
    return render(request, 'main/index.html', data)

def search_result(request):
    if request.method == "GET":
        if 'search_query' in request.GET:
            search_query = request.GET['search_query']
            documents_result = []
            news_result = []
            ad_result = []
            documents_result += Documents.objects.filter( documents_title__icontains  = search_query )
            documents_result += Documents.objects.filter ( documents_text__icontains = search_query )
            documents_result += Documents.objects.filter ( documents_publication_date__icontains = search_query )
            news_result += News.objects.filter ( news_title__icontains = search_query )
            news_result += News.objects.filter ( news_text__icontains = search_query )
            news_result += News.objects.filter ( news_publication_date__icontains = search_query )
            ad_result += Advertisements.objects.filter ( ad_title__icontains = search_query )
            ad_result += Advertisements.objects.filter ( ad_text__icontains = search_query )
            ad_result += Advertisements.objects.filter ( ad_publication_date__icontains = search_query )
            return render(request, 'main/search_results.html', {'documents_result': documents_result, 'news_result': news_result, 'ad_result': ad_result})
        else: 
            return render(request, 'main/search_results.html')
    
def historical_background(request):
    return render(request, 'main/historical_background.html')

def open_data(request):
    return render(request, 'main/open_data.html')

def executive_committee(request):
    return render(request, 'main/executive_сommittee.html')