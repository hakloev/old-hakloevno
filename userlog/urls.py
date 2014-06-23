from django.conf.urls import patterns, include, url
from views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loevdalnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    #url(r'event/(?P<id>[0-9]+)/$', event_by_id, name="event_by_id"),
)
