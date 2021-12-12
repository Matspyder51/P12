from datetime import datetime
from django.utils.timezone import make_aware
from rest_framework import viewsets, mixins
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .permissions import ClientPermissions, ContractPermission, EventPermission
from .models import Client, Contract, Event
from .serializers import ClientSerializer, ClientListSerializer, ContractSerializer, ContractListSerializer, EventSerializer, EventListSerializer
from .filters import ContractFilter, EventFilter


class CustomFilterableListMixin:

    def list(self, request, filter=None, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if filter is not None:
            queryset = queryset.filter(**filter)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_list_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_list_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_list_serializer(self, *args, **kwargs):
        serializer_class = self.list_serializer_class
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)

class CustomUpdatableMixin:

    def perform_update(self, serializer):
        serializer.save(updated_at=make_aware(datetime.now()))

class ClientViewSet(CustomFilterableListMixin, CustomUpdatableMixin, viewsets.ModelViewSet):
    
    permissions_classes = [IsAuthenticated, ClientPermissions]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    list_serializer_class = ClientListSerializer
    filterset_fields = [
        'id',
        'firstname',
        'lastname',
        'company_name',
        'sales_contact',
        'email',
        'converted'
    ]

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)


class ContractViewSet(CustomFilterableListMixin, mixins.RetrieveModelMixin, CustomUpdatableMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, ContractPermission]
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    list_serializer_class = ContractListSerializer
    filterset_class = ContractFilter

class EventViewSet(CustomFilterableListMixin, mixins.RetrieveModelMixin, CustomUpdatableMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, EventPermission]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    list_serializer_class = EventListSerializer
    filterset_class = EventFilter
