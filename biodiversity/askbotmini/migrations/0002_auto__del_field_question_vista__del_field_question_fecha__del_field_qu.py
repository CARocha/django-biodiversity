# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Question.vista'
        db.delete_column('askbotmini_question', 'vista')

        # Deleting field 'Question.fecha'
        db.delete_column('askbotmini_question', 'fecha')

        # Deleting field 'Question.pregunta'
        db.delete_column('askbotmini_question', 'pregunta')

        # Adding field 'Question.question'
        db.add_column('askbotmini_question', 'question', self.gf('django.db.models.fields.CharField')(default='', max_length=300), keep_default=False)

        # Adding field 'Question.date_created'
        db.add_column('askbotmini_question', 'date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 2, 25, 15, 31, 19, 737723)), keep_default=False)

        # Adding field 'Question.last_answer_date'
        db.add_column('askbotmini_question', 'last_answer_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 2, 25, 15, 31, 19, 737793)), keep_default=False)

        # Adding field 'Question.views'
        db.add_column('askbotmini_question', 'views', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Deleting field 'Answer.respuesta'
        db.delete_column('askbotmini_answer', 'respuesta')

        # Adding field 'Answer.answer'
        db.add_column('askbotmini_answer', 'answer', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Question.vista'
        raise RuntimeError("Cannot reverse this migration. 'Question.vista' and its values cannot be restored.")

        # Adding field 'Question.fecha'
        db.add_column('askbotmini_question', 'fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 2, 25, 14, 1, 46, 330504)), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Question.pregunta'
        raise RuntimeError("Cannot reverse this migration. 'Question.pregunta' and its values cannot be restored.")

        # Deleting field 'Question.question'
        db.delete_column('askbotmini_question', 'question')

        # Deleting field 'Question.date_created'
        db.delete_column('askbotmini_question', 'date_created')

        # Deleting field 'Question.last_answer_date'
        db.delete_column('askbotmini_question', 'last_answer_date')

        # Deleting field 'Question.views'
        db.delete_column('askbotmini_question', 'views')

        # User chose to not deal with backwards NULL issues for 'Answer.respuesta'
        raise RuntimeError("Cannot reverse this migration. 'Answer.respuesta' and its values cannot be restored.")

        # Deleting field 'Answer.answer'
        db.delete_column('askbotmini_answer', 'answer')


    models = {
        'askbotmini.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'askbotmini.question': {
            'Meta': {'object_name': 'Question'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 2, 25, 15, 31, 19, 737723)'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_answer_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 2, 25, 15, 31, 19, 737793)'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'tags': ('tagging_autocomplete.models.TagAutocompleteField', [], {'max_length': '255', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'views': ('django.db.models.fields.IntegerField', [], {})
        },
        'askbotmini.view': {
            'Meta': {'object_name': 'View'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['askbotmini.Question']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['askbotmini']
