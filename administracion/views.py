from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Datos, Categoria
from posts.models import Post


def obtenerDatos():
    try:
        datos = Datos.objects.filter(estado = True).latest('fecha_creacion')
    except:
        datos = None
    return datos


def listarCategorias(): 
    try:
        cats = list(Categoria.objects.filter(
                estado = True
            ).order_by('nombre'))
    except:
        cats = None
    return cats



def elegirPorCategoria(request, pk):    
    
    try:
        posts = list(Post.objects.filter(categoria = pk).order_by('-fecha_publicacion'))
    except:
        posts = None 
    
    
    paginator = Paginator(posts,3)
    page_number = request.GET.get('page') or 1
    listaposts = paginator.get_page(page_number)
    current_page = int(page_number)
    paginas = range(1, listaposts.paginator.num_pages + 1)
    categoria = Categoria.objects.get(id = pk)

    if(len(posts) == 0):
        isPaginated = False
    else:
        isPaginated = True

    contexto = {
        'datos': obtenerDatos(),
        'categorias': listarCategorias(),        
        'listaposts': listaposts,        
        'current_page': current_page,
        'page_range': paginas,
        'is_paginatedBuscar': isPaginated,
        'categoria': categoria
        
    }
    print(contexto) 
    return render(request, 'porcategorias.html',contexto) 


def buscar(request):    
    busqueda = request.GET['buscador']
    if(busqueda == ''):
        posts = ''
    else:
        posts = Post.objects.filter(titulo__icontains=busqueda) | Post.objects.filter(contenido__icontains=busqueda)
    
    paginator = Paginator(posts,3)
    page_number = request.GET.get('page') or 1
    listaposts = paginator.get_page(page_number)
    current_page = int(page_number)
    paginas = range(1, listaposts.paginator.num_pages + 1)

    if(len(posts) == 0):
        isPaginated = False
    else:
        isPaginated = True

    contexto = {
        'datos': obtenerDatos(),
        'categorias': listarCategorias(),        
        'listaposts': listaposts,
        'busqueda': busqueda,
        'current_page': current_page,
        'page_range': paginas,
        'is_paginatedBuscar': isPaginated
        
    }
      
    return render(request, 'busqueda.html',contexto)






