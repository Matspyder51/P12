
from rest_framework import serializers, relations
from .models import Client, Contract, Event, User


class ClientListSerializer(serializers.ModelSerializer):

    sales_contact = serializers.StringRelatedField()

    class Meta:
        model = Client
        fields = [
            'id',
            'firstname',
            'lastname',
            'company_name',
            'sales_contact',
            'email',
            'url',
        ]

        read_only_fields = [
            'sales_contact'
        ]

class ContractNestedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = [
            'id',
            'url',
        ]

class ClientSerializer(serializers.ModelSerializer):

    contracts = ContractNestedSerializer(many=True, read_only=True)
    sales_contact = relations.StringRelatedField()

    class Meta:
        model = Client
        fields = [
            'id',
            'firstname',
            'lastname',
            'company_name',
            'sales_contact',
            'email',
            'phone',
            'mobile',
            'contracts',
            'created_at',
            'updated_at',
            'url',
        ]
        read_only_fields = [
            'sales_contact',
            'created_at',
            'updated_at',
        ]

class ClientNestedSerializer(serializers.ModelSerializer):

    sales_contact = relations.StringRelatedField()

    class Meta:
        model = Client
        fields = [
            'id',
            'firstname',
            'lastname',
            'company_name',
            'sales_contact',
            'url',
        ]

class UserNestedSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email'
        ]

class ContractListSerializer(serializers.ModelSerializer):

    client = ClientNestedSerializer(read_only=True)

    class Meta:
        model = Contract
        fields = [
            'id',
            'status',
            'amount',
            'client',
            'url',
        ]


class ContractSerializer(serializers.ModelSerializer):

    client = ClientNestedSerializer(read_only=True)

    class Meta:
        model = Contract
        fields = [
            'id',
            'amount',
            'payment',
            'status',
            'client',
            'created_at',
            'updated_at',
            'url',
        ]
        read_only_fields = [
            'created_at',
            'updated_at',
        ]

class EventListSerializer(serializers.ModelSerializer):

    client = ClientNestedSerializer(read_only=True)
    support_contact = UserNestedSerializer(read_only=True)

    class Meta:
        model = Event
        fields = [
            'id',
            'event_date',
            'attendees',
            'notes',
            'support_contact',
            'client',
            'url',
        ]


class EventSerializer(serializers.ModelSerializer):

    support_contact = UserNestedSerializer(read_only=True)

    class Meta:
        model = Event
        fields = [
            'support_contact',
            'attendees',
            'event_date',
            'notes',
            'created_at',
            'updated_at',
            'url'
        ]

        read_only_fields = [
            'support_contact',
            'created_at',
            'updated_at'
        ]