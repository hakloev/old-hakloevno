# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'duty'
        db.delete_table(u'cv_duty')

        # Adding model 'organization'
        db.create_table(u'cv_organization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('started', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('ended', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True)),
            ('current', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'cv', ['organization'])

        # Adding field 'quality.quality'
        db.add_column(u'cv_quality', 'quality',
                      self.gf('django.db.models.fields.CharField')(default='derp', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'duty'
        db.create_table(u'cv_duty', (
            ('current', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('duty', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('ended', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True)),
            ('started', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'cv', ['duty'])

        # Deleting model 'organization'
        db.delete_table(u'cv_organization')

        # Deleting field 'quality.quality'
        db.delete_column(u'cv_quality', 'quality')


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
        u'cv.quality': {
            'Meta': {'object_name': 'quality'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quality': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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