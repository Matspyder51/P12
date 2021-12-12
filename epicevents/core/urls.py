from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import ClientViewSet, ContractViewSet, EventViewSet

clients_router = SimpleRouter(trailing_slash=False)
clients_router.register(r"clients/?", ClientViewSet)

contracts_router = SimpleRouter(trailing_slash=False)
contracts_router.register(r"contracts/?", ContractViewSet)

events_router = SimpleRouter(trailing_slash=False)
events_router.register(r"events/?", EventViewSet)

urlpatterns = [
    path("", include(clients_router.urls)),
    path("", include(events_router.urls)),
    path("", include(contracts_router.urls))
]