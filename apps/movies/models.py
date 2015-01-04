from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    year = models.SmallIntegerField(null=True, blank=True)
    imdb = models.CharField(max_length=10, null=False, blank=False, db_index=True)
    added = models.DateField(auto_now_add=True, null=False)
    class Meta:
        permissions = (('view_movie', 'Can view movie'),) 
        ordering = ['added']

    def __unicode__(self):
        return self.title
