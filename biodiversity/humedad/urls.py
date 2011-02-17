from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('humedad.views',
    (r'^index/$', 'index'),
    (r'^humedad/$', 'grafohumedad'),
)
