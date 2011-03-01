# -*- coding: UTF-8 -*-
from django.contrib.auth.models import User
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField
from south.modelsinspector import add_introspection_rules
from django.db import models

import datetime
add_introspection_rules([], ["^tagging_autocomplete\.models\.TagAutocompleteField"])


class Question(models.Model):
    question = models.CharField(max_length=300, verbose_name='Titulo')
    description = models.TextField()
    date_created = models.DateTimeField(default=datetime.datetime.now())
    tags = TagAutocompleteField(verbose_name='Palabras Claves',help_text='Separar elementos con "," ')
    last_answer_date = models.DateTimeField(default=datetime.datetime.now())
    views = models.IntegerField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s' % self.question

    class Meta:
        verbose_name = u'Pregunta'
        verbose_name_plural = u'Preguntas'

    #Para jalar las tags
    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    def get_answer_count(self):
        if self.answer_set.all().count() == 0:
            return 0        
        return self.answer_set.all().count()

    def last_answer(self):
        return self.answer_set.latest('fecha')


class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.TextField()
    fecha = models.DateTimeField(datetime.datetime.now())
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s' % self.question
    
    class Meta:
        verbose_name = u'Respuesta'
        verbose_name_plural = u'Respuestas'

    def save(self, force_insert=False, force_update=False):
        self.question.last_answer_date = self.fecha
        self.question.save()
	super(Answer, self).save(force_insert, force_update)

class View(models.Model):
    question = models.ForeignKey(Question)
    ip = models.CharField(max_length=40)

    def __unicode__(self):
        return u'%s - %s' % (self.ip, self.question)

    class Meta:
        verbose_name = 'View'
        verbose_name_plural = 'Views'
