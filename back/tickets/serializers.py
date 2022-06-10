from rest_framework import serializers
from .models import Ticket
from django.contrib.auth import get_user_model

User = get_user_model()

class TicketSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    user = UserSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = ('comment','user',)