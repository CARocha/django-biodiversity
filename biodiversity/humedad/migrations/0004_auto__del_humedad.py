# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Humedad'
        db.delete_table('humedad_humedad')


    def backwards(self, orm):
        
        # Adding model 'Humedad'
        db.create_table('humedad_humedad', (
            ('humedad', self.gf('django.db.models.fields.FloatField')()),
            ('ano', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mes', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('humedad', ['Humedad'])


    models = {
        
    }

    complete_apps = ['humedad']
