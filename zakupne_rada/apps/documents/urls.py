from django.urls import path, include
from . import views

app_name = 'documents'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<category_or_tag>/', views.documents_detail_list, name = 'documents_detail_list'),
    path('<category_name>/<int:document_id>/', views.documents_detail, name = 'documents_detail'),
] 