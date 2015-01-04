from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from apps.movies.models import Movie
from django.utils.decorators import method_decorator
from hakloevno import settings
#from apps.movies.forms import MovieForm
# Create your views here.

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

class MovieDetailView(DetailView):
    model = Movie
    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        return context

#class AddMovie(CheckPermMixin, CreateView):
#    model = Movie
#    form_class = MovieForm
#    permission_required = 'movies.add_movie'

class DeleteMovie(CheckPermMixin, DeleteView):
    model = Movie
    permission_required = 'movies.delete_movie'
    success_url = reverse_lazy('movies:index') 
