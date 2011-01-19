# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Humedad'
        db.create_table('humedad_humedad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('humedad', ['Humedad'])


    def backwards(self, orm):
        
        # Deleting model 'Humedad'
        db.delete_table('humedad_humedad')


    models = {
        'humedad.humedad': {
            'Meta': {'object_name': 'Humedad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['humedad']
