# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Clima.lugar'
        db.delete_column('clima_clima', 'lugar_id')

        # Adding field 'Clima.zona'
        db.add_column('clima_clima', 'zona', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['diversity.Lugar']), keep_default=False)

        # Adding unique constraint on 'Clima', fields ['ano', 'semana']
        db.create_unique('clima_clima', ['ano', 'semana'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Clima', fields ['ano', 'semana']
        db.delete_unique('clima_clima', ['ano', 'semana'])

        # We cannot add back in field 'Clima.lugar'
        raise RuntimeError(
            "Cannot reverse this migration. 'Clima.lugar' and its values cannot be restored.")

        # Deleting field 'Clima.zona'
        db.delete_column('clima_clima', 'zona_id')


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
