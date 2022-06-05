from tickets import serializers
from django.shortcuts import render
from rest_framework import static
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Ticket
# Create your views here.

@api_view(['GET'])
def get_tickets(request):
    tickets = Ticket.objects.all()
    serializer = serializers.TicketListSerializer(tickets, many=True)
    return Response(serializer.data)