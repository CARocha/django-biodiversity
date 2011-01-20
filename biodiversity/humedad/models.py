# -*- coding: utf-8 -*-
from django.db import models
import datetime

CICLO_CHOICES=[]
d=0
for i in range (datetime.date.today().year,1989,-1):
	d=i
	CICLO_CHOICES.append((i,str(d)))

class Humedad(models.Model):
    mes = models.DateField()
    ano = models.IntegerField('Año',choices=CICLO_CHOICES)
    humedad = models.FloatField()
       
    class Meta:
        verbose_name_plural = "Humedad"
        
    def __unicode__(self):
        return "%s" % int(self.humedad)
