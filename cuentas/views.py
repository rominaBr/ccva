from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import View
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from cuentas.models import Perfil
from cuentas.forms import EditarPerfil, UserRegisterForm

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

@login_required
def editarPerfil(request):
    user = request.user.id
    perfil = Perfil.objects.get(user__id=user)
    info_basica_usuario = User.objects.get(id = user)
    
    if request.method == 'POST':
        form = EditarPerfil(request.POST, request.FILES, instance=perfil) 

        if form.is_valid():
            info_basica_usuario.first_name = form.cleaned_data.get('first_name')
            info_basica_usuario.last_name = form.cleaned_data.get('last_name')
            
            
            perfil.foto = form.cleaned_data.get('foto')
            perfil.descripcion = form.cleaned_data.get('descripcion')
            perfil.web = form.cleaned_data.get('web')
            perfil.facebook = form.cleaned_data.get('facebook')
            perfil.twitter = form.cleaned_data.get('twitter')

            
            perfil.save()           
            info_basica_usuario.save()

            
            return redirect('cuentas:perfil', username = request.user.username)

    else:            
        form = EditarPerfil(instance=perfil)
        
    context = {
        'first_name': info_basica_usuario.first_name,
        'form': form,

    }
    return render(request, 'modificarperfil.html', context)

class PerfilDeUsuario(View):
    def get(self, request, username, *args, **kwargs):
        user = get_object_or_404(User, username = username)
        perfil = Perfil.objects.get(user=user)

        context = {
            'userPerfil': user,
            'perfil': perfil,
        }
        print(perfil.instagram)
        return render(request, 'perfil.html', context)