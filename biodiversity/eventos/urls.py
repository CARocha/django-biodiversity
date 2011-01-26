from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('eventos.views',
                      (r'^calendario/$', 'calendario'),
                      (r'^evento/(?P<slug>[\w-]+)/$', 'evento'),
                      (r'^$', 'index'),
)
