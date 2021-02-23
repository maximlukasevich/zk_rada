from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import News

def index(request):
    news_list = News.objects.order_by('-news_publication_date')
    return render(request, 'news/news_list.html', {'news_list': news_list})

def detail(request, news_id):
    try:
        news = News.objects.get( id = news_id )
        return render(request, 'news/detail.html', {'news': news})
    except:
        raise Http404

