from django.contrib import admin
from models import Movie, UserMovie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, MovieAdmin)
admin.site.register(UserMovie)
