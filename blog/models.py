from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Category, self).save()

class Blogpost(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, db_index=True)
    ingress = models.TextField(max_length=400)
    text = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __unicode__(self):
        return '%s' % self.title
    
    def save(self):
        self.slug = slugify(self.title)
        super(Blogpost, self).save()

    @permalink
    def get_absolute_url(self):
        return ('post_by_slug', None, { 'slug': self.slug})


