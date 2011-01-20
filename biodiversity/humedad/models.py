# -*- coding: utf-8 -*-
from django.db import models

class Humedad(models.Model):
    humedad = models.FloatField()
       
    class Meta:
        verbose_name_plural = "Humedad"
        
    def __unicode__(self):
        return "%s" % int(self.humedad)
