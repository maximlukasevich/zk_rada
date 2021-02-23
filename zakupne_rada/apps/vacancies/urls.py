from django.urls import path, include
from . import views

app_name = 'vacancies'

urlpatterns = [
    path('', views.index, name = 'index'),
] 