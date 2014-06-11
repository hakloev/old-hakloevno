# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Beer'
        db.create_table(u'beertasting_beer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ibu', self.gf('django.db.models.fields.IntegerField')()),
            ('abv', self.gf('django.db.models.fields.FloatField')()),
            ('style', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['beertasting.Style'])),
            ('brewery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['beertasting.Brewery'])),
        ))
        db.send_create_signal(u'beertasting', ['Beer'])

        # Adding model 'TastingEvent'
        db.create_table(u'beertasting_tastingevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('finished', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'beertasting', ['TastingEvent'])

        # Adding M2M table for field beers on 'TastingEvent'
        m2m_table_name = db.shorten_name(u'beertasting_tastingevent_beers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tastingevent', models.ForeignKey(orm[u'beertasting.tastingevent'], null=False)),
            ('beer', models.ForeignKey(orm[u'beertasting.beer'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tastingevent_id', 'beer_id'])

        # Adding model 'BeerRating'
        db.create_table(u'beertasting_beerrating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('beer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['beertasting.Beer'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['beertasting.TastingEvent'])),
            ('rating', self.gf('django.db.models.fields.FloatField')()),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('rated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'beertasting', ['BeerRating'])

        # Adding model 'Style'
        db.create_table(u'beertasting_style', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'beertasting', ['Style'])

        # Adding model 'Brewery'
        db.create_table(u'beertasting_brewery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'beertasting', ['Brewery'])


    def backwards(self, orm):
        # Deleting model 'Beer'
        db.delete_table(u'beertasting_beer')

        # Deleting model 'TastingEvent'
        db.delete_table(u'beertasting_tastingevent')

        # Removing M2M table for field beers on 'TastingEvent'
        db.delete_table(db.shorten_name(u'beertasting_tastingevent_beers'))

        # Deleting model 'BeerRating'
        db.delete_table(u'beertasting_beerrating')

        # Deleting model 'Style'
        db.delete_table(u'beertasting_style')

        # Deleting model 'Brewery'
        db.delete_table(u'beertasting_brewery')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'beertasting.beer': {
            'Meta': {'object_name': 'Beer'},
            'abv': ('django.db.models.fields.FloatField', [], {}),
            'brewery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['beertasting.Brewery']"}),
            'ibu': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'style': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['beertasting.Style']"})
        },
        u'beertasting.beerrating': {
            'Meta': {'object_name': 'BeerRating'},
            'beer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['beertasting.Beer']"}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['beertasting.TastingEvent']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.FloatField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'beertasting.brewery': {
            'Meta': {'object_name': 'Brewery'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'beertasting.style': {
            'Meta': {'object_name': 'Style'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'beertasting.tastingevent': {
            'Meta': {'object_name': 'TastingEvent'},
            'beers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['beertasting.Beer']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'finished': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['beertasting']