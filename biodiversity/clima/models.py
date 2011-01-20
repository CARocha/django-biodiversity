# -*- coding: utf-8 -*-
from django.db import models
from biodiversity.diversity.models import *
import datetime

CICLO_CHOICES=[]
d=0
for i in range (datetime.date.today().year,2000,-1):
	d=i
	CICLO_CHOICES.append((i,str(d)))
	
CICLO_SEMANA=[]
for a in range(1,53):
    d="semana-%d" % a
    CICLO_SEMANA.append((a,str(d)))

class Clima(models.Model):
    ''' Modelo sobre el clima en las distintas
    regiones de los distintos paises o lugares
    '''
    pais = models.ForeignKey(Pais)
    lugar = models.ForeignKey(Lugar)
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
