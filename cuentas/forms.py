from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cuentas.models import Perfil


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class EditarPerfil(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(),label='Nombre', required=False)
    last_name = forms.CharField(widget=forms.TextInput(),label='Apellido', required=False)
    descripcion = forms.CharField(widget=forms.Textarea(),required=False)
    foto = forms.ImageField(required=True)
    web = forms.URLField(required=False)
    facebook = forms.URLField(required=False)
    twitter = forms.URLField(required=False)
    instagram = forms.URLField(required=False)

    class Meta:
        model = Perfil
        fields = ('first_name', 'last_name', 'foto', 'descripcion', 'web', 'facebook', 'twitter', 'instagram')
    