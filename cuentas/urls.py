from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from administracion.views import obtenerDatos, listarCategorias
from . import views

urlpatterns = [    
    path('registro/', views.register, name='registro'),
    path('login/', LoginView.as_view(template_name='login.html',extra_context={'datos':obtenerDatos, 'categorias': listarCategorias}), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('perfil/', views.profile, name='perfil'),
    path('perfil/<str:username>/', views.profile, name='perfil'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)