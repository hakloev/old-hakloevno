from django.conf.urls import patterns, include, url
from apps.movies import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name="index"),
)
