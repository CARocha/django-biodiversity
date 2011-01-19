# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Clima'
        db.create_table('clima_clima', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diversity.Pais'])),
            ('lugar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diversity.Lugar'])),
            ('t_max', self.gf('django.db.models.fields.FloatField')()),
            ('t_min', self.gf('django.db.models.fields.FloatField')()),
            ('precipitacion', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('clima', ['Clima'])


    def backwards(self, orm):
        
        # Deleting model 'Clima'
        db.delete_table('clima_clima')


    models = {
        'clima.clima': {
            'Meta': {'object_name': 'Clima'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Lugar']"}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Pais']"}),
            'precipitacion': ('django.db.models.fields.FloatField', [], {}),
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
