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
            ('mes', self.gf('django.db.models.fields.IntegerField')()),
            ('ano', self.gf('django.db.models.fields.IntegerField')()),
            ('humedad', self.gf('django.db.models.fields.FloatField')()),
            ('zona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diversity.Lugar'])),
        ))
        db.send_create_signal('humedad', ['Humedad'])


    def backwards(self, orm):
        
        # Deleting model 'Humedad'
        db.delete_table('humedad_humedad')


    models = {
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
        },
        'humedad.humedad': {
            'Meta': {'object_name': 'Humedad'},
            'ano': ('django.db.models.fields.IntegerField', [], {}),
            'humedad': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mes': ('django.db.models.fields.IntegerField', [], {}),
            'zona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Lugar']"})
        }
    }

    complete_apps = ['humedad']
