from rest_framework import serializers
from .models import Ticket

class TicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'