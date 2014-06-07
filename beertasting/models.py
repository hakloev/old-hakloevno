# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink

# Create your models here.

class TastingEvent(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField()

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('event_by_id', None, { 'id': self.id })

class Beer(models.Model):
    name = models.CharField(max_length=50)
    ibu = models.IntegerField()
    abv = models.FloatField()
    style = models.ForeignKey('beertasting.Style')
    brewery = models.ForeignKey('beertasting.Brewery')

    def __unicode__(self):
        return (u'%s av %s' % (self.name, self.brewery ))

class BeerRating(models.Model):
    beer = models.ForeignKey('beertasting.Beer')
    user = models.ForeignKey(User)
    event = models.ForeignKey('beertasting.TastingEvent')
    rating = models.FloatField()
    comment = models.TextField()
    rated = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return (u'Bruker: %s, Øl: %s, Karakter: %s' % (self.user, self.beer, self.rating))

    @permalink
    def get_absolute_url(self):
        return('rating_by_id', None, {'eid': self.event.id, 'rid': self.id })

class Style(models.Model):
    style = models.CharField(max_length=50)

    def __unicode__(self):
        return self.style

class Brewery(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
