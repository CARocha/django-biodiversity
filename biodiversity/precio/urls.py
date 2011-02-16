from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('precio.views',
                      (r'^$', 'index'),
                      (r'^grafo/(?P<tipo>\w+)/$', 'grafo'),
              )

