# -*- coding: utf-8 -*-
from django.db import models
from biodiversity.utils import get_file_path
from thumbs import ImageWithThumbsField
from biodiversity.diversity.models import Pais

class Noticias(models.Model):
    ''' Modelo que contendra las noticias del sitio
    '''
    fecha = models.DateField()
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    pais = models.ForeignKey(Pais)
    texto = models.TextField()

    class Meta:
        verbose_name_plural = "Noticias"

    def __unicode__(self):
        return self.titulo

    def adjunto(self):
        adjunto = Galeria.objects.filter(noticia__id=self.id)
        return adjunto

class Galeria(models.Model):
    ''' Modelo sobre lo que contendran las fotos
    adjuntas a las noticias
    '''
    nombre = models.CharField(max_length=200)
    adjunto = ImageWithThumbsField(upload_to=get_file_path,
                                         sizes=((250,250), (328, 213), (350,250), (132,117)), null=True, blank=True)
    noticia = models.ForeignKey(Noticias)

    fileDir = 'noticiasfotos/fotos'
    class Meta:
        verbose_name_plural = "Galeria"

    def __unicode__(self):
        return self.nombre
