from django.db import models



class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)
    fecha_modificacion = models.DateField('Fecha de Modificación', auto_now = True, auto_now_add = False)
    fecha_eliminacion = models.DateField('Fecha de Eliminación', auto_now = True, auto_now_add = False)

    class Meta:
        abstract = True

class Categoria(ModeloBase):
    nombre = models.CharField('Nombre de la Categoría', max_length = 100, unique=True)
   
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre



class Datos(ModeloBase):
    historia = models.TextField('Nosotros')
    mision = models.TextField('Misión')
    vision = models.TextField('Visión')
    telefono = models.CharField('Telefono', max_length=20)
    email = models.EmailField('Email', max_length=200)
    direccion = models.CharField('Dirección', max_length=200)
    facebook = models.URLField('Facebook', null = True, blank = True)
    twitter = models.URLField('Twitter', null = True, blank = True)   
    instagram = models.URLField('Instagram', null = True, blank = True)    

    class Meta:
        verbose_name = 'Dato'
        verbose_name_plural = 'Datos'

    def __str__(self):
        return f'Dato {self.id}'


class Cargos(ModeloBase):
    descripcion = models.CharField('Cargo', max_length=200, unique=True)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.descripcion

class Miembros(ModeloBase):
    nombre = models.CharField('Nombre', max_length=100)
    apellido = models.CharField('Apellido', max_length=150)
    foto = models.ImageField('Foto', upload_to = 'miembros/')
    cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Miembro de la Comisión Directiva'
        verbose_name_plural = 'Miembros de la Comisión Directiva'

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.cargo})'



class Enviar_Email_to (models.Model):
    asunto = models.CharField (max_length=50)
    email = models.EmailField (max_length=200)
    mensaje = models.TextField ()

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contacto'

    def __str__(self):
        return f'De: {self.email} - Asunto: {self.asunto}'
