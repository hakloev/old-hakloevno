from django.db import models
from django.utils.text import slugify

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField()
    year = models.SmallIntegerField(null=True, blank=True)
    imdb = models.CharField(max_length=10, null=False, blank=False, db_index=True)
    added = models.DateField(auto_now_add=True, null=False)
    class Meta:
        permissions = (('view_movie', 'Can view movie'),)
        ordering = ['added']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Movie, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('movie_detail', [self.slug])

    def __unicode__(self):
        return self.title
