from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
import settings
from os import path as os_path

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^biodiversity/', include('biodiversity.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^accounts/login/$', 'django.contrib.auth.views.login', name='account_login'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'diversity.views.logout_page'),
    (r'^$', 'diversity.views.index'),
    (r'^admin/', include(admin.site.urls)),
    (r'^eventos/', include('eventos.urls')),
    (r'^bioversity/', include('diversity.urls')),
    (r'^clima/', include('clima.urls')),
    (r'^precio/', include('precio.urls')),
    (r'^documentos/', include('documentos.urls')),
    (r'^noticias/', include('noticias.urls')),
    #(r'^foro/', include('forum.urls')),
    (r'^busqueda/', include('haystack.urls')),
    (r'^tagging_autocomplete/', include('tagging_autocomplete.urls')),
    (r'^foro/', include('askbotmini.urls')),
    (r'^ayuda/$', direct_to_template, {'template': 'ayuda.html'}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^files/(.*)$', 'django.views.static.serve',
                             {'document_root': os_path.join(settings.MEDIA_ROOT)}),
                           )
