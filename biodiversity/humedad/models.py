# -*- coding: utf-8 -*-
from django.db import models
from biodiversity.diversity.models import *
import datetime

CICLO_CHOICES=[(numero, numero) for numero in range(datetime.date.today().year, 2000, -1)]
CICLO_MES=((1,'Enero'),(2,'Febrero'),(3,'Marzo'),(4,'Abril'),(5,'Mayo'),
           (6,'Junio'),(7,'Julio'),(8,'Agosto'),(9,'Septiembre'),(10,'Octubre'),
           (11,'Noviembre'),(12,'Diciembre'))

class Humedad(models.Model):
    mes = models.IntegerField(choices=CICLO_MES)
    ano = models.IntegerField('Año',choices=CICLO_CHOICES)
    humedad = models.FloatField('Humedad de suelo')
    zona = models.ForeignKey(Lugar)
       
    class Meta:
        verbose_name_plural = "Humedad de suelo"
        app_label = 'Humedad de suelo'
        db_table = 'humedad_humedad' 
        unique_together = ['ano', 'mes']
        
    def __unicode__(self):
        return "%s" % int(self.humedad)
