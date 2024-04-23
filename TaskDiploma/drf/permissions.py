from rest_framework import permissions


class TrelloUndercutPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        elif view.action == 'list':
            return request.user.is_authenticated
        elif request.method == 'POST':
            return request.user.is_authenticated
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False


    def has_object_permission(self, request, view, obj):

        if not request.user.is_authenticated:
            return False
        elif view.action == 'retrieve':
            return request.user.is_authenticated
        elif view.action == 'update':
            return (
                    obj.performer == request.user or
                    request.user.is_superuser
            )
        elif view.action == 'destroy':
            return request.user.is_superuser
        else:
            return False

class UsersCreateTrelloUndercutPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        elif view.action == 'list':
            return request.user.is_authenticated
        elif view.action == 'create':
            return request.user.is_authenticated
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return False
        else:
            return False


