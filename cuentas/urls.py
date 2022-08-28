from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from cuentas.views import editarPerfil, PerfilDeUsuario
from . import views

urlpatterns = [    
    path('registro/', views.register, name='registro'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('perfil/<username>', PerfilDeUsuario.as_view(), name='perfil'), 
    path('perfil/modificar/', editarPerfil, name='modificarperfil'),   
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)