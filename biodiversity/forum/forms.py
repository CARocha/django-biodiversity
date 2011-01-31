from django import forms
from models import *

class TopicForm(forms.ModelForm):
    class Meta:
		model = Thread
		exclude = ['forum', 'author', 'posts', 'visto', 'slug', 'time', 'latest_post_time', ]

class PostForm(forms.ModelForm):
    class Meta:
		model = Post
		exclude = ['forum', 'thread', 'author', 'time', ]

