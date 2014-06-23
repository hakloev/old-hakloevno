# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Site'
        db.create_table(u'userlog_site', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal(u'userlog', ['Site'])


    def backwards(self, orm):
        # Deleting model 'Site'
        db.delete_table(u'userlog_site')


    models = {
        u'userlog.site': {
            'Meta': {'object_name': 'Site'},
            'changed': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['userlog']