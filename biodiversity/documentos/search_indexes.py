from haystack.indexes import *
from haystack import site
from models import Documentos
import datetime

class DocumentosIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    titulo = CharField(model_attr='titulo')
    resumen = CharField(model_attr='resumen')
    palabra = CharField(model_attr='palabra_clave')
    fecha = DateField(model_attr='fecha')

    def get_queryset(self):
        return Documentos.objects.filter(fecha__lte=datetime.datetime.now())

site.register(Documentos, DocumentosIndex)
