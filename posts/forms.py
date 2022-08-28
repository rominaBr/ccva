from django import forms
from .models import Post, Comentarios



class PostForm(forms.ModelForm):        

    class Meta:
        model = Post
        fields = ['titulo', 'categoria', 'contenido','imagen_referencial']
        

class ComentForm(forms.ModelForm):
  

    class Meta:
        model=Comentarios
        fields= ['comentario']