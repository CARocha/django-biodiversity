from django.conf.urls.defaults import *
from forum.views import *
from os import path as os_path
from django.conf import settings


urlpatterns = patterns('forum.views',
    (r'^$', 'index'),
    (r'^(?P<slug>[-\w]+)/$', 'forum_list'),
    (r'^(?P<slug>[-\w]+)/(?P<t_slug>[-\w]+)/$', 'forum_detail'),
    (r'^(?P<slug>[-\w]+)/post/new/$', 'new_topic'),
    (r'^(?P<slug>[-\w]+)/(?P<t_slug>[-\w]+)/post/reply/$', 'topic_reply'),
)

