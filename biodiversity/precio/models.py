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

class UnidadInternacional(models.Model):
    '''Modelo de unidades internacionales'''
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Unidad Internacional'
        verbose_name_plural = 'Unidades Internacionales'

    def __unicode__(self):
        return self.nombre
        
class UnidadProducto(models.Model):
    ''' Modelo sobre las diferentes unidades de los
    bananos que son ingresados por los usuarios
    '''
    nombre = models.CharField(max_length=200)
    equivalente = models.FloatField('equivalente en unidad internacional')
    unidad_int = models.ForeignKey(UnidadInternacional)
        
    class Meta:
        verbose_name_plural = "Unidad del Producto"

    def __unicode__(self):
        return self.nombre

class Producto(models.Model):
    ''' Modelo sobre los nombres de los productos
    por el momento solo va ser para los bananos
    '''
    nombre = models.CharField(max_length=200)
    #variedad = models.ForeignKey(Variedad)
    
    class Meta:
        verbose_name_plural = "Productos"

    def __unicode__(self):
        return self.nombre
        
class Moneda(models.Model):
    codigo = models.CharField(max_length=3, unique=True)
    nombre = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Tipos de Moneda"
        
    def __unicode__(self):
        return self.nombre
        
class Precios(models.Model):
    
    titulo = models.CharField(max_length=200, help_text="Aca va el titulo de los precios ejem: precios correspondiente al mes de Enero")
    zona = models.ForeignKey(Lugar, blank=True, null=True, editable=False)
    
    def __unicode__(self):
        return self.titulo
        
    class Meta:
        verbose_name_plural = "Precios"
        
class PrecioConsumidor(models.Model):
    ''' Modelos sobre los distintos precios
    de los productos
    '''
    zona = models.ForeignKey(Lugar, editable=False)
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

    def unidad_to_int(self):
        return (self.precio_consumidor/self.unidad.equivalente, 
                self.unidad.unidad_int)

    def save(self, *args, **kwargs):
        try:
            if not self.zona:
                self.zona=self.precios1.zona
        except:
            self.zona=self.precios1.zona
        super(PrecioConsumidor, self).save(*args, **kwargs)

    def to_int(self):
        precio, unidad_int = self.unidad_to_int()
        try:
            tipo_de_cambio = TipoCambio.objects.filter(moneda_local = self.moneda, fecha = self.fecha)[0] 
            precio_int = precio * tipo_de_cambio.cantidad_extranjera
        except:
            tipo_de_cambio = 0
            precio_int = 0
        return (precio_int, unidad_int)
        
        
class Precio(models.Model):
    ''' Modelos sobre los distintos precios
    de los productos
    '''
    zona = models.ForeignKey(Lugar, editable=False)
    fecha = models.DateField()
    producto = models.ForeignKey(Producto)
    unidad = models.ForeignKey(UnidadProducto)
    moneda = models.ForeignKey(Moneda)
    precio_productor = models.FloatField('Precio a Productor')
    precios2 = models.ForeignKey(Precios)
    
    class Meta:
        verbose_name_plural = "Precio Productor"

    def save(self, *args, **kwargs):
        try:
            if not self.zona:
                self.zona=self.precios2.zona
        except:
            self.zona=self.precios2.zona
        super(Precio, self).save(*args, **kwargs)
   
    def __unicode__(self):
        return self.producto.nombre

    def unidad_to_int(self):
        return (self.precio_productor/self.unidad.equivalente, 
                self.unidad.unidad_int)

    def to_int(self):
        precio, unidad_int = self.unidad_to_int()
        try:
            tipo_de_cambio = TipoCambio.objects.filter(moneda_local = self.moneda, fecha = self.fecha)[0] 
            precio_int = precio * tipo_de_cambio.cantidad_extranjera
        except:
            tipo_de_cambio = 0
            precio_int = 0

        return (precio_int, unidad_int)

class TipoCambio(models.Model):
    cantidad_local = models.FloatField('Ingrese cantidad en moneda local')
    moneda_local = models.ForeignKey(Moneda)
    cantidad_extranjera = models.FloatField('Ingrese cantidad en moneda extranjera')
    moneda_extranjera= models.ForeignKey(Moneda, related_name="tipocambio_moneda")
    fecha = models.DateField(auto_now=True)

    class Meta: 
        verbose_name = "Tipo de cambio"
        verbose_name_plural = "Tipos de cambios"
        unique_together = ['moneda_local', 'moneda_extranjera', 
                           'fecha']

    def __unicode__(self):
        return "conversion de %s a %s para %s" % (self.moneda_local.nombre, 
                self.moneda_extranjera.nombre, self.fecha)

    def to_local(monto):
        local = (self.cantidad_local * monto)/self.cantidad_extranjera
        return local 
    
    def to_extran(monto):
        extran = (monto * self.cantidad_extranjera)/self.cantidad_local
        return extran
