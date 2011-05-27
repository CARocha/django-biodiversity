# -*- coding: utf-8 -*-
from django.db import models
from thumbs import ImageWithThumbsField
from biodiversity.utils import get_file_path 

class Pais(models.Model):
    ''' Modelo para contener todos los paises
        que esten en este sistema
    '''
    nombre = models.CharField(max_length=200)
    codigo_int = models.CharField('Codigo Internacional', max_length=2, help_text="Ejemplo > Nicaragua = ni")
      
    class Meta:
        verbose_name_plural = "Pais"
        app_label = "Datos Generales"
        db_table = 'diversity_pais'

    def __unicode__(self):
        return self.nombre

    def get_zonas(self):
        return Lugar.objects.filter(pais = self)

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
    descripcion = models.TextField('Descripción', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Zonas"
        verbose_name = "Zona"
        app_label = "Datos Generales"
        db_table = 'diversity_lugar'
    
    def __unicode__(self):
        return '%s, %s' % (self.nombre, self.pais.nombre)

#class FotosLugar(models.Model):
#    lugar = models.ForeignKey(Lugar)
#    foto = ImageWithThumbsField(
#    class Meta:
#        verbose_name_plural = "Fotos de Zonas"
#        verbose_name = "Foto de Zona"
#        app_label = "Datos Generales"
#        db_table = 'diversity_fotoszona'

class Socios(models.Model):
    ''' Modelo que contendra un pegueño perfil de las 
    organizaciones socias
    '''
    zona = models.ManyToManyField(Lugar)
    nombre = models.CharField(max_length=200)
    link = models.URLField(null=True, blank=True)
    logotipo = ImageWithThumbsField(upload_to=get_file_path,
               sizes=((150,150),(200,175)), null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    
    fileDir = 'socios/logos'
    
    class Meta:
        verbose_name = "Socios"
        verbose_name_plural = "Socio"
        app_label = "Datos Generales"
        db_table = 'diversity_socios'

    def __unicode__(self):
        return self.nombre
        
class TextoInicio(models.Model):
    ''' modelos del blabla del inicio de 
        bioversity
    '''
    titulo = models.CharField(max_length=200)   
    texto = models.TextField()
    
    def __unicode__(self):
        return  self.titulo
        
    class Meta:
        verbose_name_plural = "Texto del Inicio"
        app_label = "Datos Generales"
        db_table = 'diversity_textoinicio'
