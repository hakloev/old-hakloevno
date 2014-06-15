from django.conf.urls import patterns, include, url
from views import index, newpost, post_by_slug

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loevdalnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^new/$', newpost, name='newpost'),
    url(r'^posts/(?P<slug>[-a-zA-Z0-9]+)/$', post_by_slug, name='post_by_slug'),
)
