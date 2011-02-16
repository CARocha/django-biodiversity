# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Noticias.autor'
        db.add_column('noticias_noticias', 'autor', self.gf('django.db.models.fields.CharField')(default='', max_length=200), keep_default=False)

        # Adding field 'Noticias.pais'
        db.add_column('noticias_noticias', 'pais', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['diversity.Pais']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Noticias.autor'
        db.delete_column('noticias_noticias', 'autor')

        # Deleting field 'Noticias.pais'
        db.delete_column('noticias_noticias', 'pais_id')


    models = {
        'diversity.pais': {
            'Meta': {'object_name': 'Pais'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'noticias.galeria': {
            'Meta': {'object_name': 'Galeria'},
            'adjunto': ('biodiversity.noticias.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'noticia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['noticias.Noticias']"})
        },
        'noticias.noticias': {
            'Meta': {'object_name': 'Noticias'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Pais']"}),
            'texto': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['noticias']
