# -*- coding: UTF-8 -*-
from django.contrib.auth.models import User
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField
from south.modelsinspector import add_introspection_rules
from django.db import models

import datetime
add_introspection_rules([], ["^tagging_autocomplete\.models\.TagAutocompleteField"])


class Question(models.Model):
    question = models.CharField(max_length=300, verbose_name='Title')
    description = models.TextField()
    date_created = models.DateTimeField(default=datetime.datetime.now())
    tags = TagAutocompleteField(help_text='Separar elementos con "," ')
    last_answer_date = models.DateTimeField(default=datetime.datetime.now())
    views = models.IntegerField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s' % self.pregunta

    class Meta:
        verbose_name = u'Pregunta'
        verbose_name_plural = u'Preguntas'

    #Para jalar las tags
    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

class Answer(models.Model):
    question = models.IntegerField(Question)
    answer = models.TextField()
    fecha = models.DateTimeField(datetime.datetime.now())
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s' % self.respuesta

    class Meta:
        verbose_name = u'Respuesta'
        verbose_name_plural = u'Respuestas'

class View(models.Model):
    question = models.ForeignKey(Question)
    ip = models.CharField(max_length=40)

    def __unicode__(self):
        return u'%s - %s' % (self.ip, self.question)

    class Meta:
        verbose_name = 'View'
        verbose_name_plural = 'Views'