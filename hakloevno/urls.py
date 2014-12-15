from django.conf.urls import patterns, include, url
from apps.front.views import index, bus_times, bus_stops
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loevdalnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('apps.auth.urls', namespace="auth")),
    url(r'^$', index),
    url(r'^bustimes/$', bus_times),
    url(r'^busstops/', bus_stops),
    url(r'^blog/', include('apps.blog.urls', namespace='blog')), # This can be deleted, but leave it temporarily 'cause it is easy
    url(r'^tasting/', include('apps.beertasting.urls', namespace='tasting')),
    url(r'^cv/', include('apps.cv.urls', namespace='cv')),
    ) 
