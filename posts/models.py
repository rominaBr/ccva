import os
from tkinter import N
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
from ckeditor.fields import RichTextField
from administracion.models import ModeloBase, Categoria
from cuentas.models import User
from django.contrib import admin


def post_directory_path_image(instance, filename):
    image_picture_name = 'post/{0}/image.jpg'.format(instance.slug)
    full_path = os.path.join(settings.MEDIA_ROOT, image_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)
    
    return image_picture_name

class Post(ModeloBase):
    titulo = models.CharField('Título del Post', max_length=150)
    slug = models.CharField('Slug', max_length=150, unique=True, blank=True)    
    autor = models.ForeignKey(User, on_delete= models.CASCADE, related_name='posts')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    contenido = RichTextField()
    imagen_referencial = models.ImageField('Imagen Referencial', upload_to = post_directory_path_image)    
    publicado = models.BooleanField('Publicado/No Publicado', default=True)
    fecha_publicacion = models.DateField('Fecha de publicación', auto_now = False, auto_now_add = True)
    likes = models.ManyToManyField(User, blank= True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank= True, related_name='dislikes')
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ["-fecha_publicacion"]

    def __str__(self):
        return self.titulo

    def __unicode__(self):
        return self.slug


def nueva_url(instance, url=None):

    slug = slugify(instance.titulo)

    if url is not None:
        slug = url

    qs = Post.objects.filter(slug=slug).order_by("-id")

    if qs.exists():
        nueva_url_2 = "%s-%s"%(slug,qs.first().id)
        return nueva_url(instance, url=nueva_url_2)
    
    return slug

def url_creada(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = nueva_url(instance)

pre_save.connect(url_creada, sender=Post)



class Comentarios(models.Model):
    comentario = models.TextField('Comentario')
    creado = models.DateTimeField('Fecha de publicación', auto_now = False, auto_now_add = True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='autor_comentario')
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank= True, related_name='likes_comentario')
    dislikes = models.ManyToManyField(User, blank= True, related_name='dislikes_comentario')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank= True, null= True, related_name='+')

    @property
    def children(self):
        return Comentarios.objects.filter(parent=self).order_by('-creado').all()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
    
    def __str__(self):
        return f'{self.post.slug} {self.autor}'