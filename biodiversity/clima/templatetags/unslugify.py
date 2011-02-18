from django.template.defaultfilters import stringfilter
from django import template

register = template.Library()

@stringfilter
def unslugify(value):
    return value.replace('_', ' ').capitalize()

register.filter('unslugify', unslugify)
