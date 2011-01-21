# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Documentos.palabra_clave'
        db.add_column('documentos_documentos', 'palabra_clave', self.gf('django.db.models.fields.CharField')(default=None, max_length=200), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Documentos.palabra_clave'
        db.delete_column('documentos_documentos', 'palabra_clave')


    models = {
        'documentos.adjunto': {
            'Meta': {'object_name': 'Adjunto'},
            'adjunto': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'documento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentos.Documentos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'documentos.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'documentos.documentos': {
            'Meta': {'object_name': 'Documentos'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'palabra_clave': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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
