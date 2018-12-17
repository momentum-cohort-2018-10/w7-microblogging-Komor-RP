from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only post posters can edit their posts
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.poster == request.user


class IsLikerOrReadOnly(permissions.BasePermission):
    """
    Only owners of likes can dislike them
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
