from rest_framework import serializers
from .models import Movie
from django.contrib.auth import get_user_model

User = get_user_model()

class MovieSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    user = UserSerializer(read_only=True)

    class Meta:
        model = Movie
        fields = ('tmdb_id','poster_path','title','genre_ids','user',)