from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'^login/$', login_view, name="login"),
    url(r'^logout/$', logout_view, name="logout"),
)
