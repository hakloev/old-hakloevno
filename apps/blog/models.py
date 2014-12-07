from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify
import datetime

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=25, db_index=True)
    slug = models.SlugField(db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Category, self).save()

    @permalink
    def get_absolute_url(self):
        return('category_by_slug', (), {
            'slug': slugify(self.slug)
        })

class Blogpost(models.Model):
    title = models.CharField(max_length=23, unique=True)
    slug = models.SlugField(unique=True, db_index=True)
    ingress = models.TextField(max_length=400)
    text = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, blank=False)

    def __unicode__(self):
        return '%s' % self.title
    
    def save(self):
        if not self.posted:
            date = datetime.datetime.today()
            self.posted = date
        else:
            date = self.posted
        self.slug = '/%s/%s/%s/%s' % (date.year, date.month, date.day, slugify(self.title))
        super(Blogpost, self).save()
   
    @permalink
    def get_absolute_url(self):
        return ('post_by_slug', (), {
            'year': self.posted.year,
            'month': self.posted.month,
            'day': self.posted.day,
            'slug': slugify(self.title)
            })
