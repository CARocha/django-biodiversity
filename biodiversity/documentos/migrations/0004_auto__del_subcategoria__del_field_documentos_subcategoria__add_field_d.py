# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'SubCategoria'
        db.delete_table('documentos_subcategoria')

        # Deleting field 'Documentos.subcategoria'
        db.delete_column('documentos_documentos', 'subcategoria_id')

        # Adding field 'Documentos.categoria'
        db.add_column('documentos_documentos', 'categoria', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['documentos.Categoria']), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'SubCategoria'
        db.create_table('documentos_subcategoria', (
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documentos.Categoria'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('documentos', ['SubCategoria'])

        # We cannot add back in field 'Documentos.subcategoria'
        raise RuntimeError(
            "Cannot reverse this migration. 'Documentos.subcategoria' and its values cannot be restored.")

        # Deleting field 'Documentos.categoria'
        db.delete_column('documentos_documentos', 'categoria_id')


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
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentos.Categoria']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'palabra_clave': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'publico': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'resumen': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['documentos']
