# -*- coding: utf-8 -*-
from django.db import models
from biodiversity.diversity.models import *
import datetime

CICLO_CHOICES=[(numero, numero) for numero in range(datetime.date.today().year, 2000, -1)]
CICLO_SEMANA=[(numero ,("semana-%d" % numero)) for numero in range (1, 53)]

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
    
    def __unicode__(self):
        return "%s %s" % int(self.t_max, self.t_min)
        
    class Meta:
        verbose_name_plural = "Clima"
        unique_together = ['ano', 'semana']
