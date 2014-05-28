from django.db import models
from django.db.models import permalink

# Create your models here.

class Blogpost(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    ingress = models.CharField(max_length=100)
    text = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('post_by_slug', None, { 'slug': self.slug})

class Category(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)

    def __unicode__(self):
        return '%s' % self.title
