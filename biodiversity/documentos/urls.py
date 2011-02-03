from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('documentos.views',
                      (r'^privados/$', 'privados'),
                      (r'^$', 'publicos'),
                      (r'^categoria/(?P<categoria_id>\d+)/$', 'categoria'),
                      (r'^documento/(?P<documento_id>\d+)/$', 'documento'),
              )

