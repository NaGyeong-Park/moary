from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = 'tickets'

urlpatterns = [
    path('',views.create_or_get_tickets),
    path('<int:ticket_pk>/',views.read_or_edit_ticket),
]
# /+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)