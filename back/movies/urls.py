from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = 'movies'

urlpatterns = [
    path('',views.create_movie),
]
# /+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)