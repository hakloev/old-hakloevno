# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'intrest'
        db.delete_table(u'cv_intrest')

        # Deleting model 'licence'
        db.delete_table(u'cv_licence')

        # Deleting model 'language'
        db.delete_table(u'cv_language')

        # Deleting model 'quality'
        db.delete_table(u'cv_quality')


    def backwards(self, orm):
        # Adding model 'intrest'
        db.create_table(u'cv_intrest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('intrest', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'cv', ['intrest'])

        # Adding model 'licence'
        db.create_table(u'cv_licence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('licence', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'cv', ['licence'])

        # Adding model 'language'
        db.create_table(u'cv_language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'cv', ['language'])

        # Adding model 'quality'
        db.create_table(u'cv_quality', (
            ('quality', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'cv', ['quality'])


    models = {
        u'cv.education': {
            'Meta': {'object_name': 'education'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ended': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'started': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'cv.organization': {
            'Meta': {'object_name': 'organization'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'ended': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'started': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'cv.work': {
            'Meta': {'object_name': 'work'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'ended': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'started': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'work': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['cv']