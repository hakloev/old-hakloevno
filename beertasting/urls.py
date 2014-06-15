from django.conf.urls import patterns, include, url
from views import index, event_by_id, beer_rating, event_stats, event_list

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loevdalnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'event/(?P<id>[0-9]+)/$', event_by_id, name="event_by_id"),
    url(r'event/(?P<eid>[0-9]+)/beer/(?P<code>[a-z0-9]+)/$', beer_rating, name="beer_rating"),
    url(r'event/(?P<eid>[0-9]+)/stats/$', event_stats, name="event_stats"),
    url(r'event/(?P<eid>[0-9]+)/list/$', event_list, name="event_list"),
    #url(r'^newpost/$', newpost),
    #url(r'^posts/(?P<slug>[-a-zA-Z0-9]+)/$', post_by_slug, name='post_by_slug'),
)
