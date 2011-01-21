# -*- coding: utf-8 -*-
from django.db import models
import datetime

CICLO_CHOICES=[]
d=0
for i in range (datetime.date.today().year,2000,-1):
	d=i
	CICLO_CHOICES.append((i,str(d)))
	
CICLO_MES=((1,'Enero'),(2,'Febrero'),(3,'Marzo'),(4,'Abril'),(5,'Mayo'),
           (6,'Junio'),(7,'Julio'),(8,'Agosto'),(9,'Septiembre'),(10,'Octubre'),
           (11,'Noviembre'),(12,'Diciembre'))

class Humedad(models.Model):
    mes = models.IntegerField(choices=CICLO_MES)
    ano = models.IntegerField('Año',choices=CICLO_CHOICES)
    humedad = models.FloatField('Humedad de suelo')
       
    class Meta:
        verbose_name_plural = "Humedad de suelo"
        
    def __unicode__(self):
        return "%s" % int(self.humedad)
