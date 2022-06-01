from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    gender = models.BooleanField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    private = models.BooleanField(default=False)
    introduce = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to = "images/", null=True, blank=True)

    def __str__(self):
        return str(self.username)
