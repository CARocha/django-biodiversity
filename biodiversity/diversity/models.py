# -*- coding: utf-8 -*-
from django.db import models
from thumbs import ImageWithThumbsField
from biodiversity.utils import get_file_path 

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
    	return self.nombre
    	
    class Meta:
		verbose_name_plural = "Pais"

class Lugar(models.Model):
    nombre = models.CharField(max_length=200)
    pais = models.ForeignKey(Pais)
    latitud = models.DecimalField('Latitud', max_digits=8, decimal_places=5, blank=True, null = True)
    longitud = models.DecimalField('Longitud', max_digits=8, decimal_places=5, blank=True, null = True)
    
    def __unicode__(self):
    	return self.nombre
    	
    class Meta:
    	verbose_name_plural = "Lugar"

class Variedad(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
    	return self.nombre
    	
    class Meta:
    	verbose_name_plural = "Variedad"

class UnidadProducto(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
    	return self.nombre
    	
    class Meta:
    	verbose_name_plural = "Unidad del Producto"

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    variedad = models.ForeignKey(Variedad)
    unidad = models.ForeignKey(UnidadProducto)
    
    def __unicode__(self):
    	return self.nombre
    	
    class Meta:
    	verbose_name_plural = "Productos"

class Precio(models.Model):
    pais = models.ForeignKey(Pais)
    lugar = models.ForeignKey(Lugar)
    fecha = models.DateField()
    producto = models.ForeignKey(Producto)
    precio = models.FloatField()
    
    def __unicode__(self):
    	return self.producto.nombre
    	
    class Meta:
    	verbose_name_plural = "Precio"
   
class Clima(models.Model):
    fecha = models.DateField()
    pais = models.ForeignKey(Pais)
    lugar = models.ForeignKey(Lugar)
    t_max = models.FloatField('Temperatura Max.')
    t_min = models.FloatField('Temperatura Min.')
    Presi = models.FloatField('Presipitación')
    humedad = models.FloatField('Humedad en %')
    
    def __unicode__(self):
    	return "%s %s" % int(self.t_max, self.t_min)

class Socios(models.Model):
    lugar = models.ForeignKey(Lugar)
    nombre = models.CharField(max_length=200)
    link = models.URLField(null=True, blank=True)
    logotipo = ImageWithThumbsField(upload_to=get_file_path,
               sizes=((150,150),(250,250)), null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    
    def __unicode__(self):
    	return self.nombre
    	
	class Meta:
		verbose_name_plural = "Socios"

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
    	return self.nombre
    	
    class Meta:
    	verbose_name_plural = "Categoria"

class Documentos(models.Model):
    fecha = models.DateField()
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    publico = models.BooleanField()
    privado = models.BooleanField()
    adjunto = models.FileField(upload_to=get_file_path, null=True, blank=True)
    
    def __unicode__(self):
    	return self.titulo
    	
    class Meta:
    	verbose_name_plural = "Documentos"

class Galeria(models.Model):
    nombre = models.CharField(max_length=200)
    adjunto = models.FileField(upload_to=get_file_path, null=True, blank=True)
    
    def __unicode__(self):
    	return self.nombre
    	
    class Meta:
    	verbose_name_plural = "Galeria"

class Noticias(models.Model):
    fecha = models.DateField()
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    galeria = models.ForeignKey(Galeria)
    
    def __unicode__(self):
    	return self.titulo
    	
    class Meta:
    	verbose_name_plural = "Noticias"
