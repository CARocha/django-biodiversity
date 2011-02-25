from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('askbotmini.views',
            (r'^$', 'index'),
            (r'^questions/ask/$', 'ask_question'),
            #(r'^$', 'index'),
)


