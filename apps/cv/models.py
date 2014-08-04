from django.db import models

# Create your models here.

class education(models.Model): 
    started = models.IntegerField(max_length=4) 
    ended = models.IntegerField(max_length=4, blank=True, null=True) 
    current = models.BooleanField(default=False)
    school = models.CharField(max_length=50)
    url = models.URLField()
    description = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % (self.school)

class work(models.Model):
    started = models.IntegerField(max_length=4) 
    ended = models.IntegerField(max_length=4, blank=True, null=True)   
    current = models.BooleanField(default=False)
    position = models.CharField(max_length=50)
    work = models.CharField(max_length=50)
    url = models.URLField()
    description = models.CharField(max_length=500)

    def __unicode__(self):
        return u'%s %s' % (self.work, self.position)

class organization(models.Model):
    started = models.IntegerField(max_length=4)
    ended = models.IntegerField(max_length=4, blank=True, null=True)   
    current = models.BooleanField(default=False)
    position = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    url = models.URLField()
    description = models.CharField(max_length=500)
    
    def __unicode__(self):
        return u'%s %s' % (self.organization, self.position)
