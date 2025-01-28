from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    Others can view it.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS are 'GET', 'HEAD', and 'OPTIONS' - allow everyone to view
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object
        return obj.created_by == request.user
