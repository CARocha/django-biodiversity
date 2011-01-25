# encoding: utf-8

import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Producto.unidad'
        db.delete_column('precio_producto', 'unidad_id')

        # Deleting field 'Precio.precio'
        db.delete_column('precio_precio', 'precio')

        # Adding field 'Precio.unidad'
        db.add_column('precio_precio', 'unidad', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['precio.UnidadProducto']), keep_default=False)

        # Adding field 'Precio.precio_productor'
        db.add_column('precio_precio', 'precio_productor', self.gf('django.db.models.fields.FloatField')(default=None), keep_default=False)

        # Adding field 'Precio.precio_consumidor'
        db.add_column('precio_precio', 'precio_consumidor', self.gf('django.db.models.fields.FloatField')(default=None), keep_default=False)


    def backwards(self, orm):
        
        # We cannot add back in field 'Producto.unidad'
        raise RuntimeError(
            "Cannot reverse this migration. 'Producto.unidad' and its values cannot be restored.")

        # We cannot add back in field 'Precio.precio'
        raise RuntimeError(
            "Cannot reverse this migration. 'Precio.precio' and its values cannot be restored.")

        # Deleting field 'Precio.unidad'
        db.delete_column('precio_precio', 'unidad_id')

        # Deleting field 'Precio.precio_productor'
        db.delete_column('precio_precio', 'precio_productor')

        # Deleting field 'Precio.precio_consumidor'
        db.delete_column('precio_precio', 'precio_consumidor')


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
        'precio.moneda': {
            'Meta': {'object_name': 'Moneda'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'precio.precio': {
            'Meta': {'object_name': 'Precio'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moneda': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.Moneda']"}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Pais']"}),
            'precio_consumidor': ('django.db.models.fields.FloatField', [], {}),
            'precio_productor': ('django.db.models.fields.FloatField', [], {}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.Producto']"}),
            'unidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.UnidadProducto']"}),
            'zona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Lugar']"})
        },
        'precio.producto': {
            'Meta': {'object_name': 'Producto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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
