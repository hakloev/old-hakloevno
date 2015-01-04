import requests
import json
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from apps.movies.models import Movie
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
        return Movie.objects.all().order_by('-id')[:3]

class MovieDetailView(DetailView):
    model = Movie
    def get_object(self):
        qs = self.get_queryset()
        slug = self.kwargs.get('slug')
        qs = qs.filter(slug=slug)
        try:
            movie = qs.get()
        except Movie.DoesNotExist:
            return Http404
        except Movie.MultipleObjectsReturned:
            messages.error(self.request, 'Duplicates of this movie exists in the database')
            movie = qs[0]
        return movie
    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        return context

class BrowseView(CheckPermMixin, ListView):
    template_name = 'movies/movies_browse.html'
    model = Movie
    permission_required = 'movies.view_movie'
    context_object_name = 'movie_list'
    paginate_by = 10

class AddMovie(CheckPermMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name_suffix = '_create_form'
    permission_required = 'movies.add_movie'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.object.imdb:
            # Get from IMDb ID
            api_request = requests.get(API_URL + "i=%s&plot=full&r=json" % (self.object.imdb))
            if (api_request.status_code == requests.codes.ok):
                data = json.loads(api_request.text)
                if data.get('Response') == 'False':
                    messages.error(self.request, 'No movie with the ID: %s found in the API' % (self.object.imdb))
                    return HttpResponseRedirect(reverse('movies:index'))
                else:
                    self.object.title = data.get('Title', 'Unknown')
                    self.object.year = data.get('Year', 'N/A')
                    self.object.plot = data.get('Plot', 'N/A')
                    self.object.rating = data.get('imdbRating', 'N/A')
                    self.object.runtime = data.get('Runtime', 'N/A')
                    self.object.poster_url = data.get('Poster', '')
                    self.object.from_api = True
        self.object.save()
        return HttpResponseRedirect(reverse('movies:movie_detail', args=(self.object.slug,)))

@permission_required('movies.add_movie')
def add_imdb(request, id):
    api_request = requests.get(API_URL + "i=%s&plot=full&r=json" % (id))
    if (api_request.status_code == requests.codes.ok):
        data = json.loads(api_request.text)
        if data.get('Response') == 'False':
            messages.error(self.request, 'No movie with the ID: %s found in the API' % (id))
            return HttpResponseRedirect(reverse('movies:index'))
        else:
            movie = Movie(
                title=data.get('Title', 'Unknown'),
                year=data.get('Year', 'N/A'),
                plot=data.get('Plot', 'N/A'),
                rating=data.get('imdbRating', 'N/A'),
                runtime=data.get('Runtime', 'N/A'),
                poster_url=data.get('Poster', ''),
                from_api=True,
                imdb=id
            )
            movie.save()
            messages.success(request, '%s added to collection' % movie.title)
            return HttpResponseRedirect(reverse('movies:movie_detail', args=(movie.slug,)))
    messages.error(request, 'Could not add movie, try again!')        
    return HttpResponseRedirect(reverse('movies:index'))

class EditMovie(CheckPermMixin, UpdateView):
    model = Movie
    template_name_suffix = '_update_form'
    fields = ['seen', 'last_seen',]
    permission_required = 'movies.change_movie'
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(reverse('movies:movie_detail', args=(self.object.slug,)))

class DeleteMovie(CheckPermMixin, DeleteView):
    model = Movie
    permission_required = 'movies.delete_movie'
    success_url = reverse_lazy('movies:index') 

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
            context.update({'results': Movie.objects.filter(title__icontains=query)})
        else:
            messages.error(request, 'The search query must be larger than 3 characters.')
    return render(request, 'movies/movie_search.html', context)




