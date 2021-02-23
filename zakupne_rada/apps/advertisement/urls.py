from django.urls import path, include
from . import views

app_name = 'advertisement'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:ad_id>/', views.detail, name = 'detail'),
]