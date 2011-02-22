# -*- coding: utf-8 -*-
from django.db import models
from biodiversity.diversity.models import *
import datetime

CICLO_CHOICES=[(numero, numero) for numero in range(datetime.date.today().year, 2000, -1)]
CICLO_SEMANA=[(numero ,("semana-%d" % numero)) for numero in range (1, 53)]
CICLO_MES=((1,'Enero'),(2,'Febrero'),(3,'Marzo'),(4,'Abril'),(5,'Mayo'),
           (6,'Junio'),(7,'Julio'),(8,'Agosto'),(9,'Septiembre'),(10,'Octubre'),
           (11,'Noviembre'),(12,'Diciembre'))

class Climas(models.Model):
        
    class Meta:
        verbose_name_plural = "Clima"
        
    def temperatura(self):
        mostrar = Clima.objects.filter(climas__id=self.id).t_max
        print mostrar
        mostrar1 = Clima.objects.filter(climas__id=self.id).t_min
        print mostrar1
        return "Max: %s - Min: %s" % (mostrar, mostrar1)
    temperatura.short_description = 'Temperaturas Max - Min'
    
    def presipitacion(self):
        presi = Clima.objects.filter(climas__id=self.id).precipitacion
        print presi
        lista = []
        for a in presi:
            lista.append(a)        
        return lista
        print lista
    presipitacion.short_description = 'Precipitación'
    
    def zonas(self):
        zona = Clima.objects.filter(climas__id=self.id).zona.nombre
        return "%s" % (zona)
    zonas.short_description = 'Zona'
    
    def paises(self):
        pais = Clima.objects.filter(climas__id=self.id).pais.nombre
        return "%s" % (pais)
    paises.short_description = 'Pais'

class Clima(models.Model):
    ''' Modelo sobre el clima en las distintas
    regiones de los distintos paises o lugares
    '''
    pais = models.ForeignKey(Pais)
    zona = models.ForeignKey(Lugar)
    semana = models.IntegerField(choices=CICLO_SEMANA)
    ano = models.IntegerField('Año', choices=CICLO_CHOICES)
    t_max = models.FloatField('Temperatura Max.')
    t_min = models.FloatField('Temperatura Min.')
    precipitacion = models.FloatField('Precipitación',
            help_text = "Total en mm acumulada")
    climas = models.ForeignKey(Climas)
    
#    def __unicode__(self):
#        return "%s %s" % int(self.t_max, self.t_min)
        
    class Meta:
        verbose_name_plural = "Clima"
        unique_together = ['ano', 'semana']
        
class Humedad(models.Model):
    mes = models.IntegerField(choices=CICLO_MES)
    ano = models.IntegerField('Año',choices=CICLO_CHOICES)
    humedad = models.FloatField('Humedad de suelo')
    zona = models.ForeignKey(Lugar)

    class Meta:
        verbose_name_plural = "Humedad de suelo"
        unique_together = ['ano', 'mes']
        
    def __unicode__(self):
        return "%s" % int(self.humedad)
