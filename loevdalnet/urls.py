from django.conf.urls import patterns, include, url
from apps.front.views import index, busTimes
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loevdalnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'denied.html'}),
    url(r'^accounts/logout/(?P<next_page>.*)$', 'django.contrib.auth.views.logout', name='auth_logout'),
    url(r'^$', index),
    url(r'^bus/$', busTimes),
    url(r'^blog/', include('apps.blog.urls', namespace='blog')),
    url(r'^tasting/', include('apps.beertasting.urls', namespace='tasting')),
    url(r'^cv/', include('apps.cv.urls', namespace='cv')),
    ) 
