from django.shortcuts import render
from rest_framework import viewsets
from .models import Client, Contract, Event
from .serializers import ClientListSerializer, ContractListSerializer, EventListSerializer

# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractListSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
