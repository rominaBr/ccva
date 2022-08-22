import os
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


def user_directory_path_profile(instance, filename):
    profile_picture_name = 'users/{0}/profile.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)
    
    return profile_picture_name

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    descripcion = models.TextField('Descripción', null = True, blank = True)
    foto = models.ImageField('Foto', default='imagenes/perfilsinfoto.png', upload_to=user_directory_path_profile)
    web = models.URLField('Web', null = True, blank = True)
    facebook = models.URLField('Facebook', null = True, blank = True)
    twitter = models.URLField('Twitter', null = True, blank = True)
    instagram = models.URLField('Instagram', null = True, blank = True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):                       
        return f'{self.user}'


