from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from apps.movies.models import Movie

# Create your views here.
class IndexView(ListView):
    template_name = 'movies/index.html'
    model = Movie
