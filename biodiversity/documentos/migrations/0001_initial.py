# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Categoria'
        db.create_table('documentos_categoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('documentos', ['Categoria'])

        # Adding model 'SubCategoria'
        db.create_table('documentos_subcategoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documentos.Categoria'])),
        ))
        db.send_create_signal('documentos', ['SubCategoria'])

        # Adding model 'Documentos'
        db.create_table('documentos_documentos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subcategoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documentos.SubCategoria'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('resumen', self.gf('django.db.models.fields.TextField')()),
            ('publico', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('adjunto', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('documentos', ['Documentos'])


    def backwards(self, orm):
        
        # Deleting model 'Categoria'
        db.delete_table('documentos_categoria')

        # Deleting model 'SubCategoria'
        db.delete_table('documentos_subcategoria')

        # Deleting model 'Documentos'
        db.delete_table('documentos_documentos')


    models = {
        'documentos.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'documentos.documentos': {
            'Meta': {'object_name': 'Documentos'},
            'adjunto': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publico': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'resumen': ('django.db.models.fields.TextField', [], {}),
            'subcategoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentos.SubCategoria']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'documentos.subcategoria': {
            'Meta': {'object_name': 'SubCategoria'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentos.Categoria']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['documentos']
