 # -*- coding: UTF-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
#from tagging.fields import TagField
#from tagging.models import *
#from tagging_autocomplete.models import TagAutocompleteField
from thumbs import ImageWithThumbsField
from biodiversity.utils import get_file_path 

# Regla para que funcionen las migraciones de south con los campos de django-tagging
#from south.modelsinspector import add_introspection_rules
#add_introspection_rules = ([], ["^tagging_autocomplete\.models\.TagAutocompleteField"]) 

class Evento(models.Model):
    '''Modelo que representa el tipo de contenido Noticias'''
    titulo = models.CharField('Título', max_length = 120,
                               unique = True,blank = False, null = False)
    slug = models.SlugField(max_length = 120, unique = True,
                            help_text = 'unico Valor',editable=False)
    fecha_inicio = models.DateTimeField('Fecha de Inicio',blank = False, null = False,
            help_text='La hora debe presentarse en hora militar 13 = 1pm, 14 = 2pm etc..')
    fecha_final = models.DateTimeField('Fecha Final',blank = False, null = False, 
            help_text='La hora debe presentarse en hora militar 13 = 1pm, 14 = 2pm etc..')
    lugar = models.CharField('Lugar', max_length = 150,blank = True, null = True)
    contenido = models.TextField('Contenido',blank = True, null = True)
    #tags =  TagAutocompleteField(help_text='Separar elementos con "," ')
    foto = ImageWithThumbsField(upload_to=get_file_path,
                                         sizes=((150,150),(250,250)), null=True, blank=True)
    contacto = models.CharField(max_length=250, blank=True, null=True, help_text="Nombre y correo o numero de telefono del responsable" )

    def __unicode__(self):
        return self.titulo

    def get_full_url(self):
        return "/eventos/evento/%s/" % self.slug

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
    
    def save(self, force_insert=False, force_update=False):
        try:
            Evento.objects.get(pk=self.id)
        except:
            n = Evento.objects.all().count()
            self.slug = str(n) + '-' + slugify(self.titulo)
        super(Evento, self).save(force_insert, force_update)

    #override del metodo delete para eliminar el objeto de las tags tambien
    #def delete(self):
    #    taggedItem = TaggedItem.objects.get(object_id=self.id)
    #    taggedItem.delete()
    #    super(Evento, self).delete()

    #Para jalar las tags
    #def set_tags(self, tags):
    #    Tag.objects.update_tags(self, tags)

    #def get_tags(self, tags):
    #    return Tag.objects.get_for_object(self)  

    #metodo url del objeto
    def get_full_url(self):
        return "/eventos/evento/%s/" % self.slug

    #metodo para obtener el nombre del objeto
    def get_name(self):
        return self.titulo
