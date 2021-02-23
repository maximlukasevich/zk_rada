from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('advertisement/', include('advertisement.urls')),
    path('documents/', include('documents.urls')),
    path('gallery/', include('gallery.urls')),
    path('contacts/', include('contacts.urls')),
    path('vacancies/', include('vacancies.urls')),
    path('appeal/', include('appeal.urls')),
    path('receptionSchedule/', include('receptionSchedule.urls')),
    path('deputies/', include('deputies.urls')),
    path('admin/', admin.site.urls),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
