from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include(('administracion.urls','base'))),
    path('cuentas/', include(('cuentas.urls','cuentas'))), 
    path('posts/', include(('posts.urls','posts'))), 
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve , {
            'document_root':settings.MEDIA_ROOT,
        })
    ]
