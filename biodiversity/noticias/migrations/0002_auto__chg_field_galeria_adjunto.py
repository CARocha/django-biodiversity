# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Galeria.adjunto'
        db.alter_column('noticias_galeria', 'adjunto', self.gf('biodiversity.noticias.thumbs.ImageWithThumbsField')(max_length=100, null=True))


    def backwards(self, orm):
        
        # Changing field 'Galeria.adjunto'
        db.alter_column('noticias_galeria', 'adjunto', self.gf('django.db.models.fields.files.FileField')(default=None, max_length=100))


    models = {
        'noticias.galeria': {
            'Meta': {'object_name': 'Galeria'},
            'adjunto': ('biodiversity.noticias.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'noticia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['noticias.Noticias']"})
        },
        'noticias.noticias': {
            'Meta': {'object_name': 'Noticias'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['noticias']
