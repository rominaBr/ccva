from django import forms
from .models import Post, Comentarios
from administracion.views import obtenerDatos, listarCategorias



class PostForm(forms.ModelForm):        

    class Meta:
        model = Post
        fields = ['titulo', 'categoria', 'contenido','imagen_referencial']
        

class ComentForm(forms.ModelForm):
    comentario = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'border border-2 border-primary',
            'rows': '1',
            'placeholder': 'Escriba su comentario',
        }),
        required= True
    )

    class Meta:
        model=Comentarios
        fields= ['comentario']