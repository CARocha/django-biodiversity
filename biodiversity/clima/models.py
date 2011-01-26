# -*- coding: utf-8 -*-
from django.db import models
from biodiversity.diversity.models import *
import datetime

CICLO_CHOICES=[(numero, numero) for numero in range(datetime.date.today().year, 2000, -1)]
CICLO_SEMANA=[(numero ,("semana-%d" % numero)) for numero in range (1, 53)]

class Climas(models.Model):
        
    class Meta:
        verbose_name_plural = "Clima"
        
    def temperatura(self):
        mostrar = Clima.objects.get(climas__id=self.id).t_max
        mostrar1 = Clima.objects.get(climas__id=self.id).t_min
        return "Max: %s - Min: %s" % (mostrar, mostrar1)
    temperatura.short_description = 'Temperaturas Max - Min'
    
    def presipitacion(self):
        presi = Clima.objects.get(climas__id=self.id).precipitacion
        return "%s" % (presi)
    presipitacion.short_description = 'Precipitación'
    
    def zonas(self):
        zona = Clima.objects.get(climas__id=self.id).zona.nombre
        return "%s" % (zona)
    zonas.short_description = 'Zona'
    
    def paises(self):
        pais = Clima.objects.get(climas__id=self.id).pais.nombre
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
    
    def __unicode__(self):
        return "%s %s" % int(self.t_max, self.t_min)
        
    class Meta:
        verbose_name_plural = "Clima"
        unique_together = ['ano', 'semana']
        
