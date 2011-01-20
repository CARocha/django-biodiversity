# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Humedad.mes'
        db.add_column('humedad_humedad', 'mes', self.gf('django.db.models.fields.DateField')(default=None), keep_default=False)

        # Adding field 'Humedad.ano'
        db.add_column('humedad_humedad', 'ano', self.gf('django.db.models.fields.IntegerField')(default=None), keep_default=False)

        # Adding field 'Humedad.humedad'
        db.add_column('humedad_humedad', 'humedad', self.gf('django.db.models.fields.FloatField')(default=None), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Humedad.mes'
        db.delete_column('humedad_humedad', 'mes')

        # Deleting field 'Humedad.ano'
        db.delete_column('humedad_humedad', 'ano')

        # Deleting field 'Humedad.humedad'
        db.delete_column('humedad_humedad', 'humedad')


    models = {
        'humedad.humedad': {
            'Meta': {'object_name': 'Humedad'},
            'ano': ('django.db.models.fields.IntegerField', [], {}),
            'humedad': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mes': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['humedad']
