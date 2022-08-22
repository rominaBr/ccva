from django.urls import path
from posts.views import Inicio

urlpatterns = [
    path('', Inicio.as_view(), name='index'),    
]