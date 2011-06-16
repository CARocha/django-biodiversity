from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('clima.views',
                      (r'^$', 'index'),
#                      (r'^grafo/(?P<tipo>\w+)/$', 'grafo'),
                      (r'^humedad/$', 'grafohumedad'),
                      (r'^clima/(?P<tipo>\w+)/$', 'clima'),
                      (r'^ajax/temperatura/$', 'ajax_temperatura'),
                      (r'^ajax/humedad/$', 'ajax_humedad'),
                      (r'^ajax/humedad-relativa/$', 'ajax_humedad_relativa'),
                      (r'^ajax/precipitacion/$', 'ajax_precipitacion'),
              )

