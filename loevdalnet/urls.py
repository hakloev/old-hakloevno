from django.conf.urls import patterns, include, url
from front.views import index
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loevdalnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^accounts/logout/(?P<next_page>.*)$', 'django.contrib.auth.views.logout', name='auth_logout_next'),

    url(r'^$', index),
    url(r'^blog/', include('blog.urls')),
)
