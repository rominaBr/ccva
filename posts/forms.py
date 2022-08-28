from django import forms
from .models import Post, Comentarios



class PostForm(forms.ModelForm):        

    class Meta:
        model = Post
        fields = ['titulo', 'categoria', 'contenido','imagen_referencial']
        

class ComentForm(forms.ModelForm):
  
    comentario = forms.CharField(
        widget = forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Escriba comentario',
            }),
        required=True
    ),
    class Meta:
        model=Comentarios
        fields= ['comentario']