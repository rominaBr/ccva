from django.urls import path
from posts.views import Inicio
from .views import mision_and_vision, contact_views, ListarMiembros

urlpatterns = [
    path('', Inicio.as_view(), name='index'), 
    path('mision_and_vision/', mision_and_vision, name='mision_and_vision'),
    path ('contact/', contact_views, name='contacto'),
    path('miembros/', ListarMiembros.as_view(), name='miembros'),
]