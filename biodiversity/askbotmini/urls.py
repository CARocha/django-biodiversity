from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('askbotmini.views',
            url(r'^$', 'index', name='askbot-index'),            
            url(r'^questions/ask/$', 'ask_question', name='ask-question'),
            url(r'^questions/(?P<id>\d+)/$', 'view_question', name='view-question'),
            url(r'^questions/(?P<id>\d+)/edit/$', 'edit_question', name='edit-question'),
            url(r'^questions/(?P<question_id>\d+)/delete/$', 'delete_question', name='delete-question'),
            url(r'^posts/(?P<id>\d+)/edit/$', 'edit_answer', name='edit-answer'),
            url(r'^tagged/(?P<tag_name>\w+)/$', 'tagged_in', name='tagged-in'),
)


