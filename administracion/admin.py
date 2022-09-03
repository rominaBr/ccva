from django.contrib import admin
from .models import *


admin.site.register(Categoria)
admin.site.register(Datos)
admin.site.register(Cargos)
admin.site.register(Miembros)


@admin.register(Enviar_Email_to)
class Contacto(admin.ModelAdmin):

    readonly_fields = ('asunto', 'email', 'mensaje',)
