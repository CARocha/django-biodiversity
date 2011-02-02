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
        
class Precios(models.Model):
    
    class Meta:
        verbose_name_plural = "Precios"
        
    def precioconsumidor(self):
        mostrar = PrecioConsumidor.objects.get(precios1__id=self.id).precio_consumidor
        return "%s" % (mostrar)
    precioconsumidor.short_description = 'Precio Consumidor'
    
    def precioproductor(self):
        mostrar1 = Precio.objects.get(precios2__id=self.id).precio_productor
        return "%s" % (mostrar1)
    precioconsumidor.short_description = 'Precio Productor'
        
    def productoconsumidor(self):
        mostrar2 = PrecioConsumidor.objects.get(precios1__id=self.id).producto.nombre
        return "%s" % (mostrar2)
    precioconsumidor.short_description = 'Producto Consumidor'
    
    def productoproductor(self):
        mostrar3 = Precio.objects.get(precios2__id=self.id).producto.nombre
        return "%s" % (mostrar3)
    precioconsumidor.short_description = 'Producto Productor'
        
   
class PrecioConsumidor(models.Model):
    ''' Modelos sobre los distintos precios
    de los productos
    '''
    pais = models.ForeignKey(Pais)
    zona = models.ForeignKey(Lugar)
    fecha = models.DateField()
    producto = models.ForeignKey(Producto)
    unidad = models.ForeignKey(UnidadProducto)
    moneda = models.ForeignKey(Moneda)
    precio_consumidor= models.FloatField('Precio a Consumidor')
    precios1 = models.ForeignKey(Precios)
    
    class Meta:
        verbose_name_plural = "Precio Consumidor"
        
    def __unicode__(self):
        return self.producto.nombre
        
class Precio(models.Model):
    ''' Modelos sobre los distintos precios
    de los productos
    '''
    pais = models.ForeignKey(Pais)
    zona = models.ForeignKey(Lugar)
    fecha = models.DateField()
    producto = models.ForeignKey(Producto)
    unidad = models.ForeignKey(UnidadProducto)
    moneda = models.ForeignKey(Moneda)
    precio_productor = models.FloatField('Precio a Productor')
    precios2 = models.ForeignKey(Precios)
    
    class Meta:
        verbose_name_plural = "Precio Productor"
   
    def __unicode__(self):
        return self.producto.nombre
