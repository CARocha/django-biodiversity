# -*- coding: utf-8 -*-
from django.db import models
from biodiversity.diversity.models import *
import datetime

CICLO_CHOICES=[(numero, numero) for numero in range(datetime.date.today().year, 2000, -1)]
CICLO_SEMANA=[(numero ,("semana-%d" % numero)) for numero in range (1, 53)]
CICLO_MES=((1,'Ene'),(2,'Feb'),(3,'Mar'),(4,'Abr'),(5,'May'),
           (6,'Jun'),(7,'Jul'),(8,'Ago'),(9,'Sep'),(10,'Oct'),
           (11,'Nov'),(12,'Dic'))

CICLO_MES_AB=((1,'Ene'),(2,'Feb'),(3,'Mar'),(4,'Abr'),(5,'May'),
           (6,'Jun'),(7,'Jul'),(8,'Ago'),(9,'Sep'),(10,'Oct'),
           (11,'Nov'),(12,'Dic'))

class Climas(models.Model):
    nombre = models.CharField(max_length=200, help_text="Introduzca un titulo para estos climas ejem: climas para el mes de Enero")
    
    def __unicode__(self):
        return self.nombre        
        
    class Meta:
        verbose_name_plural = "Clima"
        
class Clima(models.Model):
    ''' Modelo sobre el clima en las distintas
    regiones de los distintos paises o lugares
    '''
    zona = models.ForeignKey(Lugar)
    semana = models.IntegerField(choices=CICLO_SEMANA)
    ano = models.IntegerField('Año', choices=CICLO_CHOICES)
    t_max = models.FloatField('Temperatura Max.')
    t_min = models.FloatField('Temperatura Min.')
    precipitacion = models.FloatField('Precipitación',
            help_text = "Total en mm acumulada")
    climas = models.ForeignKey(Climas)
    humedad = models.FloatField('Humedad relativa')
    
    class Meta:
        verbose_name_plural = "Clima"
        unique_together = ['zona', 'ano', 'semana']
        
class Humedad(models.Model):
    zona = models.ForeignKey(Lugar)
    mes = models.IntegerField(choices=CICLO_MES)
    ano = models.IntegerField('Año',choices=CICLO_CHOICES)
    humedad = models.FloatField('Humedad de suelo')

    class Meta:
        verbose_name_plural = "Humedad de suelo"
        unique_together = ['zona', 'ano', 'mes']
        
    def __unicode__(self):
        return "Humedad para %s en el mes %s del  %s" % (self.zona.nombre, self.mes, self.ano)
