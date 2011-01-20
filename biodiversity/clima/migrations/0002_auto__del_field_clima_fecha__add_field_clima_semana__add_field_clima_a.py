# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Clima.fecha'
        db.delete_column('clima_clima', 'fecha')

        # Adding field 'Clima.semana'
        db.add_column('clima_clima', 'semana', self.gf('django.db.models.fields.IntegerField')(default=None), keep_default=False)

        # Adding field 'Clima.ano'
        db.add_column('clima_clima', 'ano', self.gf('django.db.models.fields.IntegerField')(default=None), keep_default=False)


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Clima.fecha'
        raise RuntimeError("Cannot reverse this migration. 'Clima.fecha' and its values cannot be restored.")

        # Deleting field 'Clima.semana'
        db.delete_column('clima_clima', 'semana')

        # Deleting field 'Clima.ano'
        db.delete_column('clima_clima', 'ano')


    models = {
        'clima.clima': {
            'Meta': {'object_name': 'Clima'},
            'ano': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Lugar']"}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Pais']"}),
            'precipitacion': ('django.db.models.fields.FloatField', [], {}),
            'semana': ('django.db.models.fields.IntegerField', [], {}),
            't_max': ('django.db.models.fields.FloatField', [], {}),
            't_min': ('django.db.models.fields.FloatField', [], {})
        },
        'diversity.lugar': {
            'Meta': {'object_name': 'Lugar'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Pais']"})
        },
        'diversity.pais': {
            'Meta': {'object_name': 'Pais'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['clima']
