from django.conf.urls.defaults import *
from django.conf import settings
from models import Encuesta

urlpatterns = patterns('bioversity.views',
    (r'^$', 'index'),
    (r'^noticias/$', 'lista_noticias'),
    (r'^noticias/(?P<noticia_id>\d+)/$', 'ver_noticia'),
    (r'^documentos/$', 'lista_documentos'),
    (r'^documentos/(?P<documento_id>\d+)/$', 'ver_documento'),
)
