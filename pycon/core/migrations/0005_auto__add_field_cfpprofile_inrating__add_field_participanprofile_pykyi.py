# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'CFPProfile.inrating'
        db.add_column('core_cfpprofile', 'inrating', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)

        # Adding field 'ParticipanProfile.pykyiv_speaker'
        db.add_column('core_participanprofile', 'pykyiv_speaker', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'ParticipanProfile.pycon_speaker'
        db.add_column('core_participanprofile', 'pycon_speaker', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'ParticipanProfile.invited_speaker'
        db.add_column('core_participanprofile', 'invited_speaker', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'ParticipanProfile.help_team'
        db.add_column('core_participanprofile', 'help_team', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'ParticipanProfile.organizator'
        db.add_column('core_participanprofile', 'organizator', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'CFPProfile.inrating'
        db.delete_column('core_cfpprofile', 'inrating')

        # Deleting field 'ParticipanProfile.pykyiv_speaker'
        db.delete_column('core_participanprofile', 'pykyiv_speaker')

        # Deleting field 'ParticipanProfile.pycon_speaker'
        db.delete_column('core_participanprofile', 'pycon_speaker')

        # Deleting field 'ParticipanProfile.invited_speaker'
        db.delete_column('core_participanprofile', 'invited_speaker')

        # Deleting field 'ParticipanProfile.help_team'
        db.delete_column('core_participanprofile', 'help_team')

        # Deleting field 'ParticipanProfile.organizator'
        db.delete_column('core_participanprofile', 'organizator')


    models = {
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
        },
        'core.cfpprofile': {
            'Meta': {'object_name': 'CFPProfile'},
            'abstract': ('django.db.models.fields.TextField', [], {}),
            'brief_biography': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.CharField', [], {'default': "'20'", 'max_length': '2'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inrating': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'oneliner': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'proposed_length': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'target_audience': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'L'", 'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'core.country': {
            'Meta': {'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.news': {
            'Meta': {'object_name': 'News'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'short': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.page': {
            'Meta': {'object_name': 'Page'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.participanprofile': {
            'Meta': {'object_name': 'ParticipanProfile'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'blog': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Country']"}),
            'date_of_registration': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'help_team': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invited_speaker': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'organizator': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'pre_party': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pycon_speaker': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pykyiv_speaker': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'python_level': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'python_years': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'ticket_barcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tshirt_size': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'twitter_name': ('django.db.models.fields.CharField', [], {'max_length': '105', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'verification_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'core.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']
