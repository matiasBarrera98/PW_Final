from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.index ,name='index'), 
    path('clientes/', views.clientes, name='clientes'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('consultas/', views.consultas, name='consultas'),
    path('medicos/', views.medicos, name='medicos'),
    path('peluqueria/', views.pelu, name='pelu'),
    path('contacto/', views.contacto, name='contacto'),
    path('vacunacion/', views.vacunacion, name='vacunacion'),
    ]   
