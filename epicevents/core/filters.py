from django_filters import rest_framework as filters
from .models import Contract, Event


class ContractFilter(filters.FilterSet):

    sort_by = filters.CharFilter(
        method='filter_sort_by',
        label="Sort by a given value (amount, -amount...)",
    )

    def filter_sorty_by(self, queryset, name, value):
        values = value.lower().split(',')
        return queryset.order_by(*values)

    class Meta:
        model = Contract
        fields = [
            'id',
            'amount',
            'client__id',
            'client__sales_contact'
        ]


class EventFilter(filters.FilterSet):

    sort_by = filters.CharFilter(
        method='filter_sort_by',
        label="Sort by a given value (event_date, -event_date...)",
    )

    def filter_sorty_by(self, queryset, name, value):
        values = value.lower().split(',')
        return queryset.order_by(*values)

    class Meta:
        model = Event
        fields = [
            'id',
            'support_contact',
            'attendees',
            'event_date',
        ]