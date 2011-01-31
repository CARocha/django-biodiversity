# -*- coding: utf-8 -*-
from django.db import models
from biodiversity.utils import get_file_path 
        
class Categoria(models.Model):
    ''' Modelos sobre las categorias de los
    documentos
    '''
    nombre = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Categorias"

    def __unicode__(self):
        return self.nombre

class Documentos(models.Model):
    ''' Modelo sobre los modelos que 
    contendran los distintos documentos
    '''
    categoria = models.ForeignKey(Categoria)
    fecha = models.DateField()
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    publico = models.BooleanField()
    palabra_clave = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Documentos"
        ordering = ['-fecha']

    def __unicode__(self):
        return self.titulo
        
class Adjunto(models.Model):
    ''' Modelo para agregar varios archivos 
    a los documentos
    '''
    adjunto = models.FileField(upload_to=get_file_path)
    documento = models.ForeignKey(Documentos)
    
    fileDir = 'documentos/'

    class Meta:
        verbose_name_plural = "Adjunto a documentos"

