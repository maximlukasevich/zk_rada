from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('search_result/', views.search_result, name = 'search_result'),
    path('historical_background/', views.historical_background, name = 'historical_background'),
    path('open_data/', views.open_data, name = 'open_data'),
    path('executive_committee/', views.executive_committee, name = 'executiveCommittee'),
]