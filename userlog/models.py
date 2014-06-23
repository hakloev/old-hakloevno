from django.db import models

# Create your models here.

class Site(models.Model):
    site = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    changed = models.DateTimeField(blank=True)

    def __unicode__(self):
        return (u'Side: %s med brukernavn: %s' % (self.site, self.username))
