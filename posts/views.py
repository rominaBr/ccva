from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import  DetailView, ListView, CreateView
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm, ComentForm
from administracion.views import obtenerDatos, listarCategorias
import random

def consulta(id):
    return Post.objects.get(id = id)


class DetallePost(DetailView):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug = slug)

        form = ComentForm()

        contexto = {
            'post': post,
            'datos': obtenerDatos(), 
            'categorias': listarCategorias(),    
            'form': form      
        }
        return render(request, 'post.html',contexto)

class Inicio(ListView):

    def get(self, request, *args, **kwargs):

        postsaux = list(Post.objects.filter(
            publicado = True
        )[:5].values_list('id', flat=True))

        posts = postsaux.copy()        
        idprincipal = ''
        idpost1 = ''
        idpost2 = ''
        idpost3 = ''
        idpost4 = ''        
       

        if(len(postsaux) >= 1):
            principal = random.choice(posts)
            posts.remove(principal)
            idprincipal = consulta(principal)            
        
        if (len(postsaux) >= 2):
                        
            post1 = random.choice(posts)
            posts.remove(post1)
            idpost1 = consulta(post1)

        if (len(postsaux) >= 3):

            post2 = random.choice(posts)
            posts.remove(post2)
            idpost2 = consulta(post2)

        if (len(postsaux) >= 4):
            post3 = random.choice(posts)
            posts.remove(post3)
            idpost3 = consulta(post3)

        if (len(postsaux) >= 5):
            post4 = random.choice(posts)
            posts.remove(post4)
            idpost4 = consulta(post4)            
            
                   
        contexto = {
            'principal': idprincipal,
            'post1': idpost1,
            'post2': idpost2,
            'post3': idpost3,
            'post4': idpost4,
            'datos': obtenerDatos(),
            'categorias': listarCategorias(),
        }            
         
        return render(request, 'index.html', contexto)

def crear_post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        file = request.FILES.get('imagen_referencial')
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = current_user            
            post.save()            
            
            post.imagen_referencial = file
            post.save()
            messages.success(request, 'Post enviado')
            return redirect('posts:todos')
    else:
        form = PostForm()
    context = {
            'datos': obtenerDatos(),
            'categorias': listarCategorias(),
            'form': form,
        }
    
    return render(request, 'crearpost.html', context)


class ListarTodosLosPosts(ListView):
    model = Post
    ordering = '-fecha_publicacion'
    context_object_name = 'listaposts'
    template_name = 'posts.html'
    paginate_by = 3


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['datos'] = obtenerDatos()
        context['categorias'] = listarCategorias()
        
        return context


class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk = pk)

        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)

        next = request.POST.get('next','/')
        return HttpResponseRedirect(next)

class AddDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk = pk)

        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)

        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        next = request.POST.get('next','/')
        return HttpResponseRedirect(next)      
