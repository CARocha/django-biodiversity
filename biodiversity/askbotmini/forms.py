from django import forms
from tagging.forms import TagField
from tagging_autocomplete.widgets import TagAutocomplete
from models import *

class AskForm(forms.ModelForm):
    tags = TagField(widget=TagAutocomplete())
    notify = forms.BooleanField(required=False)

    class Meta:
        model = Question
        exclude = ['date_created', 'views', 'user', 'last_answer_date']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ['question', 'user', 'fecha']