# Or you can inherit from BasePermission class and define your own rule for access
from rest_framework.permissions import BasePermission

class AdminsPermissions(BasePermission):
    allowed_user_roles = (User.SUPERVISOR, User.ADMINISTRATOR)

    def has_permission(self, request, view):
        is_allowed_user = request.user.role in self.allowed_user_roles
        return is_allowed_user
