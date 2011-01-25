# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing M2M table for field lugar on 'Socios'
        db.delete_table('diversity_socios_lugar')

        # Adding M2M table for field zona on 'Socios'
        db.create_table('diversity_socios_zona', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('socios', models.ForeignKey(orm['diversity.socios'], null=False)),
            ('lugar', models.ForeignKey(orm['diversity.lugar'], null=False))
        ))
        db.create_unique('diversity_socios_zona', ['socios_id', 'lugar_id'])


    def backwards(self, orm):
        
        # Adding M2M table for field lugar on 'Socios'
        db.create_table('diversity_socios_lugar', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('socios', models.ForeignKey(orm['diversity.socios'], null=False)),
            ('lugar', models.ForeignKey(orm['diversity.lugar'], null=False))
        ))
        db.create_unique('diversity_socios_lugar', ['socios_id', 'lugar_id'])

        # Removing M2M table for field zona on 'Socios'
        db.delete_table('diversity_socios_zona')


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
        'diversity.socios': {
            'Meta': {'object_name': 'Socios'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'logotipo': ('biodiversity.diversity.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zona': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['diversity.Lugar']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['diversity']
