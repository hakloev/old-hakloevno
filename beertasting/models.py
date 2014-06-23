# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models import permalink
import hashlib

# Create your models here.

def createHash(name, brewery):
    string = name + brewery
    str_to_hash = string.encode('utf-8') 
    return hashlib.md5(str_to_hash).hexdigest()[-4:]

class Beer(models.Model):
    name = models.CharField(max_length=50)
    ibu = models.IntegerField()
    abv = models.FloatField()
    style = models.ForeignKey('beertasting.Style')
    brewery = models.ForeignKey('beertasting.Brewery')
    code = models.CharField(max_length=50, blank=True)

    def save(self):
        self.code = createHash(self.name, self.brewery.name)
        super(Beer, self).save()

    def __unicode__(self):
        return (u'%s fra %s' % (self.name, self.brewery))

class TastingEvent(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    beers = models.ManyToManyField('beertasting.Beer', null=True, blank=True)
    finished = models.BooleanField()

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('event_by_id', None, { 'id': self.id })

def validate_beer_rating(rating):
    if rating < 1 or rating > 10:
        raise ValidationError('Karakter mellom 1 og 10')

class BeerRating(models.Model):
    beer = models.ForeignKey('beertasting.Beer')
    user = models.ForeignKey(User)
    event = models.ForeignKey('beertasting.TastingEvent')
    rating = models.IntegerField(validators=[validate_beer_rating])
    comment = models.TextField()
    rated = models.DateTimeField(auto_now_add=True)

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
