# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'education'
        db.create_table(u'cv_education', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('started', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('ended', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True)),
            ('current', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'cv', ['education'])

        # Adding model 'work'
        db.create_table(u'cv_work', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('started', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('ended', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True)),
            ('current', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('work', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'cv', ['work'])

        # Adding model 'duty'
        db.create_table(u'cv_duty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('started', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('ended', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True)),
            ('current', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('duty', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'cv', ['duty'])

        # Adding model 'quality'
        db.create_table(u'cv_quality', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'cv', ['quality'])

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


    def backwards(self, orm):
        # Deleting model 'education'
        db.delete_table(u'cv_education')

        # Deleting model 'work'
        db.delete_table(u'cv_work')

        # Deleting model 'duty'
        db.delete_table(u'cv_duty')

        # Deleting model 'quality'
        db.delete_table(u'cv_quality')

        # Deleting model 'intrest'
        db.delete_table(u'cv_intrest')

        # Deleting model 'licence'
        db.delete_table(u'cv_licence')

        # Deleting model 'language'
        db.delete_table(u'cv_language')


    models = {
        u'cv.duty': {
            'Meta': {'object_name': 'duty'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'duty': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ended': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'started': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'cv.education': {
            'Meta': {'object_name': 'education'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ended': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True'}),
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
            'ended': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'started': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'work': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['cv']