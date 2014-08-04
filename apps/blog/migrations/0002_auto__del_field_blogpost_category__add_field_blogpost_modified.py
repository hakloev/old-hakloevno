# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Blogpost.category'
        db.delete_column(u'blog_blogpost', 'category_id')

        # Adding field 'Blogpost.modified'
        db.add_column(u'blog_blogpost', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 6, 29, 0, 0), blank=True),
                      keep_default=False)

        # Adding M2M table for field categories on 'Blogpost'
        m2m_table_name = db.shorten_name(u'blog_blogpost_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blogpost', models.ForeignKey(orm[u'blog.blogpost'], null=False)),
            ('category', models.ForeignKey(orm[u'blog.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['blogpost_id', 'category_id'])


    def backwards(self, orm):
        # Adding field 'Blogpost.category'
        db.add_column(u'blog_blogpost', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='migration', to=orm['blog.Category']),
                      keep_default=False)

        # Deleting field 'Blogpost.modified'
        db.delete_column(u'blog_blogpost', 'modified')

        # Removing M2M table for field categories on 'Blogpost'
        db.delete_table(db.shorten_name(u'blog_blogpost_categories'))


    models = {
        u'blog.blogpost': {
            'Meta': {'object_name': 'Blogpost'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingress': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'blog.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['blog']