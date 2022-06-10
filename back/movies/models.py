from django.db import models
from django.conf import settings

class Genre(models.Model):
    genre_id = models.IntegerField()
    name = models.CharField(max_length=100)

# Create your models here.
class Movie(models.Model):
    tmdb_id = models.IntegerField(null=True)
    poster_path = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=200)
    genre_ids = models.ManyToManyField(Genre,related_name='movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    
    def __str__(self):
        return self.title