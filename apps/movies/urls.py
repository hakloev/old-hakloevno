from django.conf.urls import patterns, include, url
from apps.movies import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^add/imdb/(?P<id>[a-z0-9]+)/$', views.add_imdb, name="movie_add_imdb"),
    url(r'^browse/$', views.BrowseView.as_view(), name="movie_browse"),
    url(r'^browse/(?P<movie>[-_\w]+)/$', views.MovieDetailView.as_view(), name='movie_detail'),
    url(r'^browse/(?P<movie>[-_\w]+)/(?P<id>[-0-9]+)/edit/$', views.EditMovie.as_view(), name="movie_edit"),
    url(r'^browse/(?P<movie>[-_\w]+)/(?P<id>[-0-9]+)/delete/$', views.DeleteMovie.as_view(), name="movie_delete"),
    url(r'^search', views.search, name="movie_search"),
    url(r'^imdb/search', views.search_imdb, name="movie_search_imdb"),
)
