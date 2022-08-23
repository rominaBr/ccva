from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField
from administracion.views import obtenerDatos, listarCategorias



class PostForm(forms.ModelForm):    
    

    class Meta:
        model = Post
        fields = ['titulo', 'categoria', 'contenido','imagen_referencial']
        