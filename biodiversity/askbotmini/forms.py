from django import forms
from tagging.forms import TagField
from tagging_autocomplete.widgets import TagAutocomplete
from models import *

class AskForm(forms.ModelForm):
    tags = TagField(widget=TagAutocomplete())
    notify = forms.BooleanField()

    class Meta:
        model = Question
        exclude = ['date_created', 'views', 'user', 'last_answer_date']