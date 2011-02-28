from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('diversity.views',
    (r'^sitios/$', 'lista_sitios'),
    (r'^logout/$', 'logout_page'),
    (r'^mapa/$', 'mapa'),
    (r'^sitios/(?P<sitio_id>\d+)/$', 'ver_sitio'),
    (r'^socios/$', 'lista_socios'),
    (r'^ajax/zonas/$', 'ajax_zonas'),
    (r'^ajax/pais/(?P<pais_id>\d+)/$', 'ajax_pais'),
    (r'^ajax/socios/(?P<zona>\d+)/$', 'ajax_socios'),
    (r'^ficha/(?P<id>\d+)/$', 'ficha_socios'),
)
