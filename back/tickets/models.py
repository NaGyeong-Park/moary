from django.db import models
from movies.models import Movie
from django.conf import settings
# Create your models here.

class Ticket(models.Model):
    movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    poster = models.ImageField(upload_to='poster/',null=True, blank=True)
    peoples = models.IntegerField(default=1)
    place = models.CharField(max_length=100)
    watch_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    rate = models.IntegerField(blank=True, null=True)
    private = models.BooleanField(default=False)