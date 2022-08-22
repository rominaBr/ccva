from gc import get_objects
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from administracion.views import listarCategorias, obtenerDatos


def register(request):
    if request.method ==  'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('cuentas:login')
    else:
        form = UserRegisterForm() 

    context = {
        'form': form,
        'categorias': listarCategorias,
        'datos': obtenerDatos,
        }

    return render(request, 'registro.html', context)



def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    
    contexto = {
        'user': user,
        'posts': posts,
    }
    return render(request, 'perfil.html', contexto)