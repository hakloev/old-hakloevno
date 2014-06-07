from django.conf.urls import patterns, include, url
from views import index, event_by_id, rating_by_id

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loevdalnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'event(?P<id>[0-9]+)/$', event_by_id, name="event_by_id"),
    url(r'event(?P<eid>[0-9]+)/rating(?P<rid>[0-9]+)/$', rating_by_id, name="rating_by_id"),
    #url(r'^newpost/$', newpost),
    #url(r'^posts/(?P<slug>[-a-zA-Z0-9]+)/$', post_by_slug, name='post_by_slug'),
)
