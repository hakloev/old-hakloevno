import requests
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from apps.movies.models import Movie, UserMovie
from django.utils.decorators import method_decorator
from hakloevno import settings
from apps.movies.forms import MovieForm
# Create your views here.

API_URL = "http://www.omdbapi.com/?"

#Mixins
# http://brack3t.com/our-custom-mixins.html
class CheckPermMixin(object):
    permission_required = None
    login_url = settings.LOGIN_URL
    def dispatch(self, request, *args, **kwargs):
        has_permission = request.user.has_perm(self.permission_required)
        if not has_permission:
            messages.error(request, "You don't have access to this app!")
            return HttpResponseRedirect('%s?next=%s' % (self.login_url, self.request.path))
        return super(CheckPermMixin, self).dispatch(request, *args, **kwargs)

class IndexView(CheckPermMixin, ListView):
    template_name = 'movies/index.html'
    model = Movie
    # Required fields for CheckPermMixin
    permission_required = 'movies.view_movie'
    def get_queryset(self):
        # .order_by('?') is really expensive in large dbs, need fix
        return UserMovie.objects.filter(user=self.request.user).order_by('?')[:3]
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({'movies': UserMovie.objects.filter(user=self.request.user).count()})
        context.update({'unseen': UserMovie.objects.filter(user=self.request.user, seen=False).count()})
        return context

class MovieDetailView(DetailView):
    model = UserMovie
    def get_object(self):
        return get_object_or_404(UserMovie, user=self.request.user, movie=Movie.objects.get(slug=self.kwargs.get('movie')))
    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        return context

class BrowseView(CheckPermMixin, ListView):
    template_name = 'movies/movies_browse.html'
    model = UserMovie
    permission_required = 'movies.view_movie'
    context_object_name = 'movie_list'
    paginate_by = 10
    def get_queryset(self):
        return UserMovie.objects.filter(user=self.request.user)

@permission_required('movies.add_movie')
def add_imdb(request, id):
    api_request = requests.get(API_URL + "i=%s&plot=full&r=json" % (id))
    if (api_request.status_code == requests.codes.ok):
        data = json.loads(api_request.text)
        if data.get('Response') == 'False':
            messages.error(self.request, 'No movie with the ID: %s found in the API' % (id))
            return HttpResponseRedirect(reverse('movies:index'))
        else:
            if Movie.objects.filter(title=data.get('Title', 'Unknown')).count():
                movie = Movie.objects.get(title=data.get('Title', 'Unknown'))
            else:
                movie = Movie(
                    title=data.get('Title', 'Unknown'),
                    year=data.get('Year', 'N/A'),
                    plot=data.get('Plot', 'N/A'),
                    rating=data.get('imdbRating', 'N/A'),
                    runtime=data.get('Runtime', 'N/A'),
                    poster_url=data.get('Poster', ''),
                    imdb=id
                )
                movie.save()
            if not UserMovie.objects.filter(movie=movie, user=request.user).count():
                user_movie = UserMovie(
                    movie = movie,
                    user = request.user
                )
                user_movie.save()
                messages.success(request, '%s added to the collection' % movie.title)
            else:
                messages.error(request, 'You already have this movie in your collection')
            return HttpResponseRedirect(reverse('movies:movie_detail', args=(movie.slug,)))
    messages.error(request, 'Could not add movie, try again!')        
    return HttpResponseRedirect(reverse('movies:index'))

class EditMovie(CheckPermMixin, UpdateView):
    model = UserMovie
    template_name_suffix = '_update_form'
    fields = ['last_seen',]
    permission_required = 'movies.change_movie'
    def get_object(self):
        return get_object_or_404(UserMovie, id=self.kwargs.get('id'))
    def form_valid(self, form):
        if self.get_object().user.id == self.request.user.id:
            self.object = form.save()
            messages.success(self.request, '%s updated' % self.object.movie.title)
        else:
            messages.error(self.request, 'This is not your movie to edit')
        return HttpResponseRedirect(reverse('movies:movie_detail', args=(self.object.movie.slug,)))

class DeleteMovie(CheckPermMixin, DeleteView):
    model = UserMovie
    permission_required = 'movies.delete_movie'
    success_url = reverse_lazy('movies:index') 
    def get_object(self):
        return get_object_or_404(UserMovie, id=self.kwargs.get('id'))
    # Check possiblity to move the delete function to the model and remove UserMovie objects from there
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user.id == request.user.id:
            movie = self.object.movie.title
            if UserMovie.objects.filter(movie=self.object.movie).count() == 1:
                Movie.objects.get(slug=self.object.movie.slug).delete()
                # Automatically removes UserMovie-object
            else:
                UserMovie.objects.get(id=self.object.id).delete()          
            messages.success(request, '%s successfully removed from collection' % movie)
        else:
            messages.error(request, 'This is not your movie to delete')
        return HttpResponseRedirect(self.get_success_url())

def search_imdb(request):
    context = {}
    query = request.GET.get('q', None)
    if query:
        context.update({'query': query})
        api_request = requests.get(API_URL + 's=%s&r=json' % (query))
        if (api_request.status_code == requests.codes.ok):
            data = json.loads(api_request.text)
            if data.get('Response') == 'False':
                messages.error(request, 'No search result from API')
                return HttpResponseRedirect(reverse('movies:index'))
            else:
                context.update({'movies': data.get('Search')})
    return render(request, 'movies/movie_search_imdb.html', context)

def search(request):
    context = {}
    query = request.GET.get('q', None)
    if query:
        context.update({'query': query})
        if len(query) > 3:
            context.update({'results': UserMovie.objects.filter(movie__title__icontains=query, user=request.user)})
        else:
            messages.error(request, 'The search query must be larger than 3 characters.')
    return render(request, 'movies/movie_search.html', context)
