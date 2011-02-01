from django.conf.urls.defaults import *
from django.conf import settings
from models import Encuesta

urlpatterns = patterns('bioversity.views',
    (r'^$', 'index'),
    (r'^sitios/$', 'lista_sitios'),
    (r'^sitios/(?P<sitio_id>\d+)/$', 'ver_sitio'),
    (r'^socios/$', 'lista_socios'),
    (r'^socios/(?P<socio_id>\d+)/$', 'ver_socio'),
)
