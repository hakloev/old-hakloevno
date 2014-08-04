# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'duty.ended'
        db.alter_column(u'cv_duty', 'ended', self.gf('django.db.models.fields.IntegerField')(default=2001, max_length=4))

        # Changing field 'education.ended'
        db.alter_column(u'cv_education', 'ended', self.gf('django.db.models.fields.IntegerField')(default=2001, max_length=4))

        # Changing field 'work.ended'
        db.alter_column(u'cv_work', 'ended', self.gf('django.db.models.fields.IntegerField')(default=2001, max_length=4))

    def backwards(self, orm):

        # Changing field 'duty.ended'
        db.alter_column(u'cv_duty', 'ended', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True))

        # Changing field 'education.ended'
        db.alter_column(u'cv_education', 'ended', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True))

        # Changing field 'work.ended'
        db.alter_column(u'cv_work', 'ended', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True))

    models = {
        u'cv.duty': {
            'Meta': {'object_name': 'duty'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'duty': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ended': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'started': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'cv.education': {
            'Meta': {'object_name': 'education'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ended': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'started': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'cv.intrest': {
            'Meta': {'object_name': 'intrest'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intrest': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'cv.language': {
            'Meta': {'object_name': 'language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'cv.licence': {
            'Meta': {'object_name': 'licence'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'licence': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'cv.quality': {
            'Meta': {'object_name': 'quality'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'cv.work': {
            'Meta': {'object_name': 'work'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'ended': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'started': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'work': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['cv']