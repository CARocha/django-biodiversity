# -*- coding: utf-8 -*-
from django.db import models
from thumbs import ImageWithThumbsField
from biodiversity.utils import get_file_path 

class Pais(models.Model):
    ''' Modelo para contener todos los paises
        que esten en este sistema
    '''
    nombre = models.CharField(max_length=200)
      
    class Meta:
        verbose_name_plural = "Pais"

    def __unicode__(self):
        return self.nombre

class Lugar(models.Model):
    ''' Lugar de origen de los productos que vayan
    agregando
    '''
    nombre = models.CharField(max_length=200)
    pais = models.ForeignKey(Pais)
    latitud = models.DecimalField('Latitud', max_digits=8,
            decimal_places=5, blank=True, null = True)
    longitud = models.DecimalField('Longitud', max_digits=8,
            decimal_places=5, blank=True, null = True)

    class Meta:
        verbose_name_plural = "Lugar"
    
    def __unicode__(self):
        return self.nombre

class Socios(models.Model):
    ''' Modelo que contendra un pegueño perfil de las 
    organizaciones socias
    '''
    lugar = models.ForeignKey(Lugar)
    nombre = models.CharField(max_length=200)
    link = models.URLField(null=True, blank=True)
    logotipo = ImageWithThumbsField(upload_to=get_file_path,
               sizes=((150,150),(250,250)), null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Socios"
        verbose_name_plural = "Socio"

    def __unicode__(self):
        return self.nombre
