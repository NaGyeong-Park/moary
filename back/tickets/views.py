from .serializers import TicketSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Ticket
# Create your views here.

@api_view(['GET', 'POST'])
def create_or_get_tickets(request):
    if request.method == 'POST':
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'GET':
        # private = false로 filter 변경 필요
        tickets = Ticket.objects.filter(private=False)[::-1]
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def read_or_edit_ticket(request, ticket_pk):
    ticket = Ticket.objects.get(pk=ticket_pk)
    if request.method == 'GET':
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = TicketSerializer(ticket, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)