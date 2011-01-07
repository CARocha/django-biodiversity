# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Pais'
        db.create_table('diversity_pais', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('diversity', ['Pais'])

        # Adding model 'Lugar'
        db.create_table('diversity_lugar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diversity.Pais'])),
            ('latitud', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('longitud', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
        ))
        db.send_create_signal('diversity', ['Lugar'])

        # Adding model 'Variedad'
        db.create_table('diversity_variedad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('diversity', ['Variedad'])

        # Adding model 'UnidadProducto'
        db.create_table('diversity_unidadproducto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('diversity', ['UnidadProducto'])

        # Adding model 'Producto'
        db.create_table('diversity_producto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('variedad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diversity.Variedad'])),
            ('unidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diversity.UnidadProducto'])),
        ))
        db.send_create_signal('diversity', ['Producto'])

        # Adding model 'Precio'
        db.create_table('diversity_precio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diversity.Pais'])),
            ('lugar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diversity.Lugar'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diversity.Producto'])),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('diversity', ['Precio'])

        # Adding model 'Clima'
        db.create_table('diversity_clima', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diversity.Pais'])),
            ('lugar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diversity.Lugar'])),
            ('t_max', self.gf('django.db.models.fields.FloatField')()),
            ('t_min', self.gf('django.db.models.fields.FloatField')()),
            ('Presi', self.gf('django.db.models.fields.FloatField')()),
            ('humedad', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('diversity', ['Clima'])

        # Adding model 'Socios'
        db.create_table('diversity_socios', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lugar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diversity.Lugar'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('logotipo', self.gf('biodiversity.diversity.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True)),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal('diversity', ['Socios'])

        # Adding model 'Categoria'
        db.create_table('diversity_categoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('diversity', ['Categoria'])

        # Adding model 'Documentos'
        db.create_table('diversity_documentos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('resumen', self.gf('django.db.models.fields.TextField')()),
            ('publico', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('privado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('adjunto', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('diversity', ['Documentos'])

        # Adding model 'Noticias'
        db.create_table('diversity_noticias', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('texto', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('diversity', ['Noticias'])

        # Adding model 'Galeria'
        db.create_table('diversity_galeria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('adjunto', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('galeria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diversity.Noticias'])),
        ))
        db.send_create_signal('diversity', ['Galeria'])


    def backwards(self, orm):
        
        # Deleting model 'Pais'
        db.delete_table('diversity_pais')

        # Deleting model 'Lugar'
        db.delete_table('diversity_lugar')

        # Deleting model 'Variedad'
        db.delete_table('diversity_variedad')

        # Deleting model 'UnidadProducto'
        db.delete_table('diversity_unidadproducto')

        # Deleting model 'Producto'
        db.delete_table('diversity_producto')

        # Deleting model 'Precio'
        db.delete_table('diversity_precio')

        # Deleting model 'Clima'
        db.delete_table('diversity_clima')

        # Deleting model 'Socios'
        db.delete_table('diversity_socios')

        # Deleting model 'Categoria'
        db.delete_table('diversity_categoria')

        # Deleting model 'Documentos'
        db.delete_table('diversity_documentos')

        # Deleting model 'Noticias'
        db.delete_table('diversity_noticias')

        # Deleting model 'Galeria'
        db.delete_table('diversity_galeria')


    models = {
        'diversity.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'diversity.clima': {
            'Meta': {'object_name': 'Clima'},
            'Presi': ('django.db.models.fields.FloatField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'humedad': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Lugar']"}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Pais']"}),
            't_max': ('django.db.models.fields.FloatField', [], {}),
            't_min': ('django.db.models.fields.FloatField', [], {})
        },
        'diversity.documentos': {
            'Meta': {'object_name': 'Documentos'},
            'adjunto': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'privado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publico': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'resumen': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'diversity.galeria': {
            'Meta': {'object_name': 'Galeria'},
            'adjunto': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'galeria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Noticias']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'diversity.lugar': {
            'Meta': {'object_name': 'Lugar'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Pais']"})
        },
        'diversity.noticias': {
            'Meta': {'object_name': 'Noticias'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'diversity.pais': {
            'Meta': {'object_name': 'Pais'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'diversity.precio': {
            'Meta': {'object_name': 'Precio'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Lugar']"}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Pais']"}),
            'precio': ('django.db.models.fields.FloatField', [], {}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Producto']"})
        },
        'diversity.producto': {
            'Meta': {'object_name': 'Producto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'unidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.UnidadProducto']"}),
            'variedad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Variedad']"})
        },
        'diversity.socios': {
            'Meta': {'object_name': 'Socios'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'logotipo': ('biodiversity.diversity.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lugar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Lugar']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'diversity.unidadproducto': {
            'Meta': {'object_name': 'UnidadProducto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'diversity.variedad': {
            'Meta': {'object_name': 'Variedad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['diversity']
