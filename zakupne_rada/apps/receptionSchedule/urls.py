from django.urls import path, include
from . import views

app_name = 'receptionSchedule'

urlpatterns = [
    path('', views.index, name = 'index'),
] 