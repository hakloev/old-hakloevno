from django.conf.urls import patterns, include, url
from views import register, register_success

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loevdalnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^new/$', register, name='new_user'),
    url(r'^success/$', register_success, name='register_success'),
)
