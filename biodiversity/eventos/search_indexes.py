from haystack.indexes import *
from haystack import site
from models import Evento 
import datetime

class EventoIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    titulo = CharField(model_attr='title')
    fecha = DateField(model_attr='fecha')

    def get_queryset(self):
        return Evento.objects.filter(fecha_inicio__lte=datetime.datetime.now())

site.register(Evento, EventoIndex)
