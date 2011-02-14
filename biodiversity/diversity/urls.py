from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('diversity.views',
    (r'^sitios/$', 'lista_sitios'),
    (r'^sitios/(?P<sitio_id>\d+)/$', 'ver_sitio'),
    (r'^socios/$', 'lista_socios'),
    (r'^socios/(?P<socio_id>\d+)/$', 'ver_socio'),
    (r'^index/$', 'inicio'),
)
