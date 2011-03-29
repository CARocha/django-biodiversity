# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'Clima', fields ['ano', 'semana']
        db.delete_unique('clima_clima', ['ano', 'semana'])

        # Adding unique constraint on 'Clima', fields ['zona', 'ano', 'semana']
        db.create_unique('clima_clima', ['zona_id', 'ano', 'semana'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Clima', fields ['zona', 'ano', 'semana']
        db.delete_unique('clima_clima', ['zona_id', 'ano', 'semana'])

        # Adding unique constraint on 'Clima', fields ['ano', 'semana']
        db.create_unique('clima_clima', ['ano', 'semana'])


    models = {
        'clima.clima': {
            'Meta': {'unique_together': "(['zona', 'ano', 'semana'],)", 'object_name': 'Clima'},
            'ano': ('django.db.models.fields.IntegerField', [], {}),
            'climas': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clima.Climas']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Pais']"}),
            'precipitacion': ('django.db.models.fields.FloatField', [], {}),
            'semana': ('django.db.models.fields.IntegerField', [], {}),
            't_max': ('django.db.models.fields.FloatField', [], {}),
            't_min': ('django.db.models.fields.FloatField', [], {}),
            'zona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Lugar']"})
        },
        'clima.climas': {
            'Meta': {'object_name': 'Climas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'clima.humedad': {
            'Meta': {'unique_together': "(['ano', 'mes'],)", 'object_name': 'Humedad'},
            'ano': ('django.db.models.fields.IntegerField', [], {}),
            'humedad': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mes': ('django.db.models.fields.IntegerField', [], {}),
            'zona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Lugar']"})
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
            'codigo_int': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['clima']
