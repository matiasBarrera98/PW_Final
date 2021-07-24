from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_mascotas, name='lista'),
    path('lista/<id>', views.mascota_id, name='mascota'),
]