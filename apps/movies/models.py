import requests
import tempfile
from django.db import models
from django.utils.text import slugify
from django.core.files import File
from hakloevno import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField()
    year = models.SmallIntegerField(null=True, blank=True)
    imdb = models.CharField(max_length=10, null=False, blank=False, db_index=True)
    plot = models.TextField(blank=True)
    rating = models.FloatField(null=True, blank=True)
    from_api = models.BooleanField(default=False)
    runtime = models.CharField(max_length=10, null=True, blank=True)
    seen = models.BooleanField(default=False)
    last_seen = models.DateField(null=True, blank=True)
    poster_url = models.URLField(blank=True, null=True)
    added = models.DateField(auto_now_add=True, null=False)
    class Meta:
        permissions = (('view_movie', 'Can view movie'),)
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.poster_url and self.poster_img != '':
            import shutil
            import os
            file_save_dir = 'media/images/posters/'
            r = requests.get(self.poster_url, stream=True)
            with open(file_save_dir + '%s.jpg' % self.slug, 'wb') as handle:
                for block in r.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
            self.poster_url = '/' + file_save_dir + '%s.jpg' % self.slug
        if self.last_seen:
            self.seen = True
        return super(Movie, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('movie_detail', [self.slug])

    def __unicode__(self):
        return self.title
