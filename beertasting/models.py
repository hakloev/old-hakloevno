# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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
    rating = models.FloatField()
    comment = models.TextField()

    def __unicode__(self):
        return (u'Bruker: %s, Øl: %s, Karakter: %s' % (self.user, self.beer, self.rating))

class Style(models.Model):
    style = models.CharField(max_length=50)

    def __unicode__(self):
        return self.style

class Brewery(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
