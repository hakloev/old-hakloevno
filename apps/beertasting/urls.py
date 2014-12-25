from django.conf.urls import patterns, include, url
from views import index, event_by_id, beer_rating, event_stats, event_list, beer_stats, beer_overall, user_ratings, beer_list

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loevdalnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index, name="index"),
    url(r'^event/(?P<id>[0-9]+)/$', event_by_id, name="event_by_id"),
    url(r'^event/(?P<eid>[0-9]+)/beer/(?P<code>[a-z0-9]+)/$', beer_rating, name="beer_rating"),
    url(r'^event/(?P<eid>[0-9]+)/results/$', event_stats, name="event_stats"),
    url(r'^event/(?P<eid>[0-9]+)/admin/$', event_list, name="event_list"),
    url(r'^stats/beer/(?P<id>[0-9a-z]+)/$', beer_stats, name="beer_stats"),
    url(r'^stats/beers/$', beer_list, name="beer_list"),
    url(r'^stats/top10/$', beer_overall, name="beer_overall"),
    url(r'^user/(?P<id>[0-9]+)/ratings/$', user_ratings, name="user_ratings"),
    
    #url(r'^newpost/$', newpost),
    #url(r'^posts/(?P<slug>[-a-zA-Z0-9]+)/$', post_by_slug, name='post_by_slug'),
)
