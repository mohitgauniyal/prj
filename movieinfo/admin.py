from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ['imdb_id', 'name', 'release_date', 'genre', 'summary', 'poster']

admin.site.register(Movie, MovieAdmin)