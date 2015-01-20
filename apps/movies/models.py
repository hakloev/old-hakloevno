import requests
from django.db import models
from django.db.models import Max
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.files import File
from hakloevno import settings

POSTER_SAVE_URL = 'media/images/posters/'

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField()
    year = models.SmallIntegerField(null=True, blank=True)
    imdb = models.CharField(max_length=10, null=False, blank=False, db_index=True)
    plot = models.TextField(blank=True)
    rating = models.FloatField(null=True, blank=True)
    runtime = models.CharField(max_length=10, null=True, blank=True)
    poster_url = models.URLField(blank=True, null=True)
    class Meta:
        permissions = (('view_movie', 'Can view movie'),)
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if not self.poster_url.startswith('/media/'):
            r = requests.get(self.poster_url, stream=True)
            with open(POSTER_SAVE_URL + '%s.jpg' % self.slug, 'wb') as handle:
                for block in r.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
            self.poster_url = '/' + POSTER_SAVE_URL + '%s.jpg' % self.slug
        return super(Movie, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('movie_detail', [self.slug])

    def __unicode__(self):
        return self.title

class UserMovie(models.Model):
    um_id = models.IntegerField(editable=False, blank=True, null=True)
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(User)
    seen = models.BooleanField(default=False)
    last_seen = models.DateField(null=True, blank=True)
    added = models.DateField(auto_now_add=True, null=False)

    class Meta:
        unique_together = ('um_id', 'movie')

    def save(self, *args, **kwargs):
        um_id = UserMovie.objects.filter(user=self.user).aggregate(Max('um_id')).get('um_id__max')
        self.um_id = 1 if um_id is None else um_id + 1
        if self.last_seen:
            self.seen = True
        return super(UserMovie, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s --> %s' % (self.user, self.movie)
