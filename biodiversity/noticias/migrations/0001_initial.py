# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Noticias'
        db.create_table('noticias_noticias', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('texto', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('noticias', ['Noticias'])

        # Adding model 'Galeria'
        db.create_table('noticias_galeria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('adjunto', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('noticia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['noticias.Noticias'])),
        ))
        db.send_create_signal('noticias', ['Galeria'])


    def backwards(self, orm):
        
        # Deleting model 'Noticias'
        db.delete_table('noticias_noticias')

        # Deleting model 'Galeria'
        db.delete_table('noticias_galeria')


    models = {
        'noticias.galeria': {
            'Meta': {'object_name': 'Galeria'},
            'adjunto': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
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
