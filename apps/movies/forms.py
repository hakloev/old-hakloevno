from django import forms
from apps.movies.models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'imdb', 'year',)
