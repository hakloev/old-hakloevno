from django.conf.urls import patterns, include, url
from apps.movies import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^add/$', views.AddMovie.as_view(), name="movie_add"),
    url(r'^(?P<slug>[-_\w]+)/$', views.MovieDetailView.as_view(), name='movie_detail'),
    url(r'^(?P<slug>[-_\w]+)/edit/$', views.EditMovie.as_view(), name="movie_edit"),
    url(r'^(?P<slug>[-_\w]+)/delete/$', views.DeleteMovie.as_view(), name="movie_delete"),
)
