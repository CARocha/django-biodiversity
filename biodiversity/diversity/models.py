# -*- coding: utf-8 -*-
from django.db import models
from thumbs import ImageWithThumbsField
from biodiversity.utils import get_file_path 

# Create your models here.

class Pais(models.Model):
    ''' Modelo para contener todos los paises
        que esten en este sistema
    '''
    nombre = models.CharField(max_length=200)
	  
    def __unicode__(self):
    	return self.nombre
    	
    class Meta:
		verbose_name_plural = "Pais"

class Lugar(models.Model):
    ''' Lugar de origen de los productos que vayan
	agregando
    '''
    nombre = models.CharField(max_length=200)
    pais = models.ForeignKey(Pais)
    latitud = models.DecimalField('Latitud', max_digits=8, decimal_places=5, blank=True, null = True)
    longitud = models.DecimalField('Longitud', max_digits=8, decimal_places=5, blank=True, null = True)
    
    def __unicode__(self):
    	return self.nombre
    	
    class Meta:
    	verbose_name_plural = "Lugar"

class Variedad(models.Model):
    ''' Modelo sobre la variedad de platanos
    '''
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
    	return self.nombre
    	
    class Meta:
    	verbose_name_plural = "Variedad"

class UnidadProducto(models.Model):
    ''' Modelo sobre las diferentes unidades de los
	bananos que son ingresados por los usuarios
    '''
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
    	return self.nombre
    	
    class Meta:
    	verbose_name_plural = "Unidad del Producto"

class Producto(models.Model):
    ''' Modelo sobre los nombres de los productos
	por el momento solo va ser para los bananos
    '''
    nombre = models.CharField(max_length=200)
    variedad = models.ForeignKey(Variedad)
    unidad = models.ForeignKey(UnidadProducto)
    
    def __unicode__(self):
    	return self.nombre
    	
    class Meta:
    	verbose_name_plural = "Productos"

class Precio(models.Model):
    ''' Modelos sobre los distintos precios
	de los productos
    '''
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
    ''' Modelo sobre el clima en las distintas
	regiones de los distintos paises o lugares
    '''
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
    ''' Modelo que contendra un pegueño perfil de las 
	organizaciones socias
    '''
    lugar = models.ForeignKey(Lugar)
    nombre = models.CharField(max_length=200)
    link = models.URLField(null=True, blank=True)
    logotipo = ImageWithThumbsField(upload_to=get_file_path,
               sizes=((150,150),(250,250)), null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    
    def __unicode__(self):
    	return self.nombre
    	
    class Meta:
	verbose_name = "Socios"
	verbose_name_plural = "Socio"

class Categoria(models.Model):
    ''' Modelos sobre las categorias de los
	documentos
    '''
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
    	return self.nombre
    	
    class Meta:
    	verbose_name_plural = "Categoria"

class Documentos(models.Model):
    ''' Modelo sobre los modelos que 
	contendran los distintos documentos
    '''
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

class Noticias(models.Model):
    ''' Modelo que contendra las noticias del sitio
    '''
    fecha = models.DateField()
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    
    def __unicode__(self):
    	return self.titulo
    	
    class Meta:
    	verbose_name_plural = "Noticias"

class Galeria(models.Model):
    ''' Modelo sobre lo que contendran las fotos
	adjuntas a las noticias
    '''
    nombre = models.CharField(max_length=200)
    adjunto = models.FileField(upload_to=get_file_path, null=True, blank=True)
    galeria = models.ForeignKey(Noticias)
    
    def __unicode__(self):
    	return self.nombre
    	
    class Meta:
    	verbose_name_plural = "Galeria"
