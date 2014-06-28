from django.conf.urls import patterns, include, url
from views import all_posts, create_post, post_by_slug

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loevdalnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', create_post, name='newpost'),
    url(r'^new/$', create_post, name='newpost'),
    url(r'^posts/$', all_posts, name='allposts'),
    url(r'^posts/(?P<slug>[-a-zA-Z0-9]+)/$', post_by_slug, name='post_by_slug'),
)
