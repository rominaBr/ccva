from django.urls import path
from administracion.views import elegirPorCategoria,  buscar
from .views import DetallePost, ListarTodosLosPosts, AddDislike, AddLike, AddComentDislike, AddComentLike, ResponderComentario,BorrarComentario, EditarComentario, BorrarPost, EditarPost
from . import views


urlpatterns = [
    path('categorias/<int:pk>/', elegirPorCategoria, name='categorias'),
    path('all/', ListarTodosLosPosts.as_view(), name='todos'),
    path('busqueda/', buscar, name='buscar'),
    path('nuevo/', views.crear_post, name='nuevo'),

    path('detalle/<slug:slug>/', DetallePost.as_view(), name = 'detalle_post'),
    path('editar/<slug:slug>', EditarPost.as_view(), name="editarpost"),
    path('borrar/<slug:slug>', BorrarPost.as_view(), name="borrarpost"),
    
    path('detalle/<int:pk>/like', AddLike.as_view(), name='like'),
    path('detalle/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    
    path('detalle/<slug:slug>/comentario/<int:pk>/like', AddComentLike.as_view(), name='comentlike'),
    path('detalle/<slug:slug>/comentario/<int:pk>/dislike', AddComentDislike.as_view(), name='comentdislike'),

    path('detalle/<slug:slug>/comentario/<int:pk>/responder',ResponderComentario.as_view(), name='respondercoment'),

    path('detalle/<slug:slug>/comentario/borrar/<int:pk>/', BorrarComentario.as_view(), name="borrarcomentario"),
    path('detalle/<slug:slug>/comentario/editar/<int:pk>/', EditarComentario.as_view(), name="editarcomentario"),
    
]