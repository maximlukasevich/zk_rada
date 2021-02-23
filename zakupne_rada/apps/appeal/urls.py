from django.urls import path, include
from . import views

app_name = 'appeal'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('thanks/', views.thanks, name = 'thanks'),
]