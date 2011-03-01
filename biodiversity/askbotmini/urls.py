from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('askbotmini.views',
            (r'^$', 'index'),            
            (r'^questions/ask/$', 'ask_question'),
            (r'^questions/(?P<id>\d+)/$', 'view_question'),
            (r'^questions/(?P<id>\d+)/edit/$', 'edit_question'),
            (r'^tagged/(?P<tag_name>\w+)/$', 'tagged_in'),
)


