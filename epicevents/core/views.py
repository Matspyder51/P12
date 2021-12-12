from datetime import datetime
from django.utils.timezone import make_aware
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from .permissions import ClientPermissions, ContractPermission, EventPermission
from .models import Client, Contract, Event, User
from .serializers import ClientSerializer, ClientListSerializer, ContractSerializer, ContractListSerializer, EventSerializer, EventListSerializer
from .filters import ContractFilter, EventFilter

import random


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

class CustomUpdatableMixin(mixins.UpdateModelMixin):

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
        'email'
    ]

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)

    @action(methods=['POST', 'GET'], detail=True)
    def contracts(self, request, pk=None):
        self.check_object_permissions(request, self.get_object())
        if request.method == 'POST':
            client = self.get_object()
            serializer = ContractSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            contract = Contract(**data)
            contract.client = client
            contract.sales_contact = request.user
            contract.save()
            serializer = ContractSerializer(contract, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            queryset = Contract.objects.filter(client__pk=pk)
            page = self.paginate_queryset(queryset)
            serializer = ContractListSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)


class ContractViewSet(CustomFilterableListMixin, mixins.RetrieveModelMixin, CustomUpdatableMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, ContractPermission]
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    list_serializer_class = ContractListSerializer
    filterset_class = ContractFilter

    @action(methods=['GET', 'POST'], detail=True)
    def events(self, request, pk=None):
        self.check_object_permissions(request, self.get_object())
        if request.method == 'POST':
            contract = self.get_object()
            serializer = EventSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.validate_contract(pk)
            data = serializer.validated_data
            event = Event(**data)
            event.client = contract.client
            event.support_contact = random.choice(User.objects.all().filter(groups__name='support_team'))
            event.save()
            serializer = EventSerializer(event, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            queryset = Event.objects.filter(contract=pk)
            page = self.paginate_queryset(queryset)
            serializer = EventListSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

class EventViewSet(CustomFilterableListMixin, mixins.RetrieveModelMixin, CustomUpdatableMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, EventPermission]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    list_serializer_class = EventListSerializer
    filterset_class = EventFilter
