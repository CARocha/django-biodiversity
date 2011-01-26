# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Climas'
        db.create_table('clima_climas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clima', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clima.Clima'])),
        ))
        db.send_create_signal('clima', ['Climas'])


    def backwards(self, orm):
        
        # Deleting model 'Climas'
        db.delete_table('clima_climas')


    models = {
        'clima.clima': {
            'Meta': {'unique_together': "(['ano', 'semana'],)", 'object_name': 'Clima'},
            'ano': ('django.db.models.fields.IntegerField', [], {}),
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
            'clima': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clima.Clima']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
