# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Blogpost.title'
        db.alter_column(u'blog_blogpost', 'title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=25))

        # Changing field 'Category.title'
        db.alter_column(u'blog_category', 'title', self.gf('django.db.models.fields.CharField')(max_length=25))

    def backwards(self, orm):

        # Changing field 'Blogpost.title'
        db.alter_column(u'blog_blogpost', 'title', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True))

        # Changing field 'Category.title'
        db.alter_column(u'blog_category', 'title', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'blog.blogpost': {
            'Meta': {'object_name': 'Blogpost'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingress': ('django.db.models.fields.TextField', [], {'max_length': '400'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'})
        },
        u'blog.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '25', 'db_index': 'True'})
        }
    }

    complete_apps = ['blog']