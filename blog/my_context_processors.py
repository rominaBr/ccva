from administracion.models import Categoria, Datos, Cargos

def get_categorias_y_datos(request):

    try:
        datos = Datos.objects.filter(estado = True).latest('fecha_creacion')
    except:
        datos = None
    
    try:
        cats = list(Categoria.objects.filter(
                estado = True
            ).order_by('nombre'))
    except:
        cats = None
    
    try:
        cargos = Cargos.objects.all().order_by('id')
    except:
        cargos = None

    context = {
        'datos': datos,
        'categorias': cats,
        'cargos': cargos,
    }

    return context