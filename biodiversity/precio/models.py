# -*- coding: utf-8 -*-
from django.db import models
from biodiversity.diversity.models import *

class Variedad(models.Model):
    ''' Modelo sobre la variedad de platanos
    '''
    nombre = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Variedad"

    def __unicode__(self):
        return self.nombre
        
class UnidadProducto(models.Model):
    ''' Modelo sobre las diferentes unidades de los
    bananos que son ingresados por los usuarios
    '''
    nombre = models.CharField(max_length=200)
    equivalente = models.FloatField('equivalente en unidad internacional')
    unidad_int = models.CharField("nombre de la unidad", max_length=10)
        
    class Meta:
        verbose_name_plural = "Unidad del Producto"

    def __unicode__(self):
        return self.nombre

class Producto(models.Model):
    ''' Modelo sobre los nombres de los productos
    por el momento solo va ser para los bananos
    '''
    nombre = models.CharField(max_length=200)
    variedad = models.ForeignKey(Variedad)
    unidad = models.ForeignKey(UnidadProducto)
    
    class Meta:
        verbose_name_plural = "Productos"

    def __unicode__(self):
        return self.nombre
        
class Moneda(models.Model):
    nombre = models.CharField(max_length=200)
    
    
    class Meta:
        verbose_name_plural = "Tipos de Moneda"
        
    def __unicode__(self):
        return self.nombre
        
class Precio(models.Model):
    ''' Modelos sobre los distintos precios
    de los productos
    '''
    pais = models.ForeignKey(Pais)
    lugar = models.ForeignKey(Lugar)
    fecha = models.DateField()
    producto = models.ForeignKey(Producto)
    moneda = models.ForeignKey(Moneda)
    precio = models.FloatField()
    
    class Meta:
        verbose_name_plural = "Precio"
   
    def __unicode__(self):
        return self.producto.nombre
