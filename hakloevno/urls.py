from django.conf.urls import patterns, include, url
from apps.pages.views import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loevdalnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('apps.auth.urls', namespace="auth")),
    url(r'^bustimes/$', bus_times),
    url(r'^busstops/$', bus_stops),
    url(r'^cv/$', cv_view),
    url(r'^blog/', include('apps.blog.urls', namespace='blog')),
    url(r'^tasting/', include('apps.beertasting.urls', namespace='tasting')),
    url(r'^movies/', include('apps.movies.urls', namespace='movies')),
    ) 
