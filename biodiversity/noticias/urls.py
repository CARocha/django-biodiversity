from django.conf.urls.defaults import *
from os import path as os_path
from django.conf import settings
from noticias.views import *

urlpatterns = patterns('noticias.views',
   (r'^listar/$',  lista_noticias),
   (r'^ver/(?P<noticia_id>\d+)/$',  ver_noticia), 
 )
