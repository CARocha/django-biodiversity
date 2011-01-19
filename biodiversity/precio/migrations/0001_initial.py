# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Variedad'
        db.create_table('precio_variedad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('precio', ['Variedad'])

        # Adding model 'UnidadProducto'
        db.create_table('precio_unidadproducto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('equivalente', self.gf('django.db.models.fields.FloatField')()),
            ('unidad_int', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('precio', ['UnidadProducto'])

        # Adding model 'Producto'
        db.create_table('precio_producto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('variedad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['precio.Variedad'])),
            ('unidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['precio.UnidadProducto'])),
        ))
        db.send_create_signal('precio', ['Producto'])

        # Adding model 'Precio'
        db.create_table('precio_precio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diversity.Pais'])),
            ('lugar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diversity.Lugar'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['precio.Producto'])),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('precio', ['Precio'])


    def backwards(self, orm):
        
        # Deleting model 'Variedad'
        db.delete_table('precio_variedad')

        # Deleting model 'UnidadProducto'
        db.delete_table('precio_unidadproducto')

        # Deleting model 'Producto'
        db.delete_table('precio_producto')

        # Deleting model 'Precio'
        db.delete_table('precio_precio')


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
        'precio.precio': {
            'Meta': {'object_name': 'Precio'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Lugar']"}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Pais']"}),
            'precio': ('django.db.models.fields.FloatField', [], {}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.Producto']"})
        },
        'precio.producto': {
            'Meta': {'object_name': 'Producto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'unidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.UnidadProducto']"}),
            'variedad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.Variedad']"})
        },
        'precio.unidadproducto': {
            'Meta': {'object_name': 'UnidadProducto'},
            'equivalente': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'unidad_int': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'precio.variedad': {
            'Meta': {'object_name': 'Variedad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['precio']
