from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Categoria, Miembros
from django.views.generic import ListView
from posts.models import Post
from administracion.forms import Envio_de_Email
from django.core.mail import send_mail


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
        'listaposts': listaposts,
        'busqueda': busqueda,
        'current_page': current_page,
        'page_range': paginas,
        'is_paginatedBuscar': isPaginated
        
    }
      
    return render(request, 'busqueda.html',contexto)


def mision_and_vision (request):
    return render (request, "mision_vision.html")

def contact_views (request):
    form_email = Envio_de_Email ()
    if request.method == "POST":
        form_email = Envio_de_Email (request.POST)
        print (form_email)
        if form_email.is_valid ():
            asunto = request.POST["asunto"] #recuperado del name
            email = request.POST["email"]
            mensaje = request.POST["mensaje"]
            print (form_email) #para ver en consola que llega # borrar
            
            send_mail (
                        asunto,
                        mensaje + " enviado por: " + email,
                        'agregar correo de ccva en outlook',
                        ['aqui se agrega un correo al cual se quiere avisar'],
                        fail_silently=False,
                    )
            return redirect (request, "thank")
    return render (request, "contact.html", {"form_email":form_email})


class ListarMiembros(ListView):
    model = Miembros
    ordering = 'id'
    context_object_name = 'listamiembros'
    template_name = 'miembros.html'
    


   