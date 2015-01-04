from django.conf.urls import patterns, include, url
from apps.movies import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^(?P<slug>[-_\w]+)/$', views.MovieDetailView.as_view(), name='movie_detail'),
    url(r'^(?P<slug>[-_\w]+)/delete/$', views.DeleteMovie.as_view(), name="movie_delete"),
)
