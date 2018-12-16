from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only object owners can edit their objects(posts)
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.poster == request.user
