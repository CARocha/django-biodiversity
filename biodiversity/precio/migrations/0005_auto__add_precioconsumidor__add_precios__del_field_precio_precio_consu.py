# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'PrecioConsumidor'
        db.create_table('precio_precioconsumidor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diversity.Pais'])),
            ('zona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diversity.Lugar'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['precio.Producto'])),
            ('unidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['precio.UnidadProducto'])),
            ('moneda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['precio.Moneda'])),
            ('precio_consumidor', self.gf('django.db.models.fields.FloatField')()),
            ('precios1', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['precio.Precios'])),
        ))
        db.send_create_signal('precio', ['PrecioConsumidor'])

        # Adding model 'Precios'
        db.create_table('precio_precios', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('precio', ['Precios'])

        # Deleting field 'Precio.precio_consumidor'
        db.delete_column('precio_precio', 'precio_consumidor')

        # Adding field 'Precio.precios2'
        db.add_column('precio_precio', 'precios2', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['precio.Precios']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'PrecioConsumidor'
        db.delete_table('precio_precioconsumidor')

        # Deleting model 'Precios'
        db.delete_table('precio_precios')

        # Adding field 'Precio.precio_consumidor'
        db.add_column('precio_precio', 'precio_consumidor', self.gf('django.db.models.fields.FloatField')(default=None), keep_default=False)

        # Deleting field 'Precio.precios2'
        db.delete_column('precio_precio', 'precios2_id')


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
            'precio_productor': ('django.db.models.fields.FloatField', [], {}),
            'precios2': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.Precios']"}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.Producto']"}),
            'unidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.UnidadProducto']"}),
            'zona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Lugar']"})
        },
        'precio.precioconsumidor': {
            'Meta': {'object_name': 'PrecioConsumidor'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moneda': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.Moneda']"}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Pais']"}),
            'precio_consumidor': ('django.db.models.fields.FloatField', [], {}),
            'precios1': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.Precios']"}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.Producto']"}),
            'unidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.UnidadProducto']"}),
            'zona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Lugar']"})
        },
        'precio.precios': {
            'Meta': {'object_name': 'Precios'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
