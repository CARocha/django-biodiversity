# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FotosLugar'
        db.create_table('diversity_fotoszona', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lugar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diversity.Lugar'])),
            ('foto', self.gf('biodiversity.diversity.thumbs.ImageWithThumbsField')(max_length=100)),
        ))
        db.send_create_signal('diversity', ['FotosLugar'])


    def backwards(self, orm):
        
        # Deleting model 'FotosLugar'
        db.delete_table('diversity_fotoszona')


    models = {
        'diversity.fotoslugar': {
            'Meta': {'object_name': 'FotosLugar', 'db_table': "'diversity_fotoszona'"},
            'foto': ('biodiversity.diversity.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Lugar']"})
        },
        'diversity.lugar': {
            'Meta': {'object_name': 'Lugar'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Pais']"})
        },
        'diversity.pais': {
            'Meta': {'object_name': 'Pais'},
            'codigo_int': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'diversity.socios': {
            'Meta': {'object_name': 'Socios'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'logotipo': ('biodiversity.diversity.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zona': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['diversity.Lugar']", 'symmetrical': 'False'})
        },
        'diversity.textoinicio': {
            'Meta': {'object_name': 'TextoInicio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['diversity']
