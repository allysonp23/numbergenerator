from rest_framework.permissions import BasePermission
from rest_framework_api_key.models import APIKey


class HasValidAPIKeyOrAuthenticated(BasePermission):
    """
    Allows access to authenticated users (JWT/session) or valid API key auth.
    """
    def has_permission(self, request, view):
        # Authenticated user via JWT or session
        if request.user and request.user.is_authenticated:
            return True
        # API Key authentication: request.auth is APIKey instance on success
        if isinstance(request.auth, APIKey):
            return True
        return False
