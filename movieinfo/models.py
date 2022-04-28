from django.db import models

class Movie(models.Model):

    ACTION = 'Action'
    WAR = 'War'
    COMEDY = 'Comedy'
    SUSPENSE = 'Suspense'
    NONE = '-'

    GENRES = [
        (ACTION, 'Action'),
        (WAR, 'War'),
        (COMEDY, 'Comedy'),
        (SUSPENSE, 'Suspense'),
        (NONE, '-')
    ]

    imdb_id = models.CharField(max_length=20, primary_key=True)
    movie_link = models.URLField()
    name = models.CharField(max_length=100)
    release_date = models.DateField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    summary = models.TextField()
    genre = models.CharField(max_length=10, choices=GENRES, default=NONE)
    poster = models.ImageField(default='default.jpg', upload_to='posters')

    def __str__(self):
        return self.name