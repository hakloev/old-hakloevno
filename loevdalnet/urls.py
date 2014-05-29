from django.conf.urls import patterns, include, url
from front.views import index, login_view, login_user, logout_view
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loevdalnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', index),
    url(r'^login/$', login_view),
    url(r'^auth/user/$', login_user),
    url(r'^logout/$', logout_view),
    url(r'^blog/', include('blog.urls')),
)
