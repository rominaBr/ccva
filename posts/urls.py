from django.urls import path
from administracion.views import elegirPorCategoria,  buscar, obtenerDatos, listarCategorias
from .views import DetallePost, ListarTodosLosPosts, AddDislike, AddLike
from . import views


urlpatterns = [
    path('categorias/<int:pk>/', elegirPorCategoria, name='categorias'),
    path('all/', ListarTodosLosPosts.as_view(), name='todos'),
    path('busqueda/', buscar, name='buscar'),
    path('nuevo/', views.crear_post, name='nuevo'),
    path('detalle/<slug:slug>/', DetallePost.as_view(), name = 'detalle_post'),
    path('detalle/<int:pk>/like', AddLike.as_view(), name='like'),
    path('detalles/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    
    
]