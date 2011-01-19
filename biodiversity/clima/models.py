# -*- coding: utf-8 -*-
from django.db import models
from diversity.models import *

class Clima(models.Model):
    ''' Modelo sobre el clima en las distintas
    regiones de los distintos paises o lugares
    '''
    fecha = models.DateField()
    pais = models.ForeignKey(Pais)
    lugar = models.ForeignKey(Lugar)
    t_max = models.FloatField('Temperatura Max.')
    t_min = models.FloatField('Temperatura Min.')
    precipitacion = models.FloatField('Precipitación',
            help_text = "Total en mm acumulada")
    
    def __unicode__(self):
        return "%s %s" % int(self.t_max, self.t_min)
