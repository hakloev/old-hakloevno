from django.conf.urls import patterns, include, url
from views import all_posts, create_post, post_by_slug, post_by_year, post_by_month, post_by_day, category_by_slug

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loevdalnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', create_post, name='create_post'),
    url(r'^archive/$', all_posts, name='index'),
    url(r'^archive/(?P<year>[\d]{4})/$', post_by_year, name='post_by_year'),
    url(r'^archive/(?P<year>[\d]{4})/(?P<month>[\d]{1,2})/$', post_by_month, name='post_by_month'),
    url(r'^archive/(?P<year>[\d]{4})/(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/$', post_by_day, name='post_by_day'),
    url(r'^archive/(?P<year>[\d]{4})/(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/(?P<slug>[-a-zA-Z\d]+)/$', post_by_slug, name='post_by_slug'),
    url(r'^archive/categories/(?P<category>[-a-zA-Z\d]+)/$', category_by_slug, name='category_by_slug'),
)
