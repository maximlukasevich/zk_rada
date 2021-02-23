from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Documents, Categories, Tags, Sessions

def index(request):
    documents_sessions = Sessions.objects.all()
    documents_tags = Tags.objects.all()
    documents_categories = Categories.objects.order_by('category_name')
    data = {'documents_categories': documents_categories, 'documents_tags': documents_tags, 'documents_sessions': documents_sessions}
    return render(request, 'documents/documents_list.html', data)

def documents_detail_list(request, category_or_tag):
    try:
        documents_category_list = Documents.objects.filter( category__category_name = category_or_tag )
        documents_tag_list = Documents.objects.filter( tags__tag = category_or_tag )
        documents_sessions_list = Documents.objects.filter( session__number = category_or_tag )
        data = {'documents_category_list': documents_category_list, 'documents_tag_list': documents_tag_list, 'category_or_tag': category_or_tag, 'documents_sessions_list': documents_sessions_list}
        return render(request, 'documents/documents_detail_list.html', data)
    except: 
        not_found = ""
        return render(request, 'documents/documents_detail_list.html', {'not_found': not_found })

def documents_detail(request, category_name, document_id):
    try:
        document = Documents.objects.get( id = document_id )
        tags = document.tags.all()
        session = document.session
        data = {'document': document, 'category_name': category_name, 'tags': tags, 'session': session}
        return render(request, 'documents/detail.html', data)
    except:
        raise Http404