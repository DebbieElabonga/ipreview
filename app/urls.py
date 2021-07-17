from django.urls import path
from .views import index,profile,search_projects
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', index , name ='index'),
    path('profile/', profile, name='profile'),
    path('search/', search_projects, name='search'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)