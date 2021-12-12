from rest_framework import permissions


class ClientPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.groups.filter(name='selling_team').exists()

    def has_object_permission(self, request, view, obj):
        return request.user == obj.sales_contact


class ContractPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.client.sales_contact


class EventPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.support_contact