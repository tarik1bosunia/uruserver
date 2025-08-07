from rest_framework.permissions import BasePermission, SAFE_METHODS
from .enums import Roles


class IsAuthenticatedAndVerified(BasePermission):
    """
    Base permission to check if user is authenticated and has a verified email.
    """

    def is_verified(self, user):
        return getattr(user, "is_authenticated", False) and getattr(user, "is_email_verified", False)

    def has_permission(self, request, view):
        return self.is_verified(request.user)


class IsVerifiedSuperAdmin(IsAuthenticatedAndVerified):
    """
    Allows access only to authenticated SuperAdmin users with verified email.
    """
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == Roles.SUPERADMIN


class IsVerifiedStudent(IsAuthenticatedAndVerified):
    """
    Allows access only to authenticated Student users with verified email.
    """
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == Roles.STUDENT


class IsVerifiedTeacher(IsAuthenticatedAndVerified):
    """
    Allows access only to authenticated Teacher users with verified email.
    """
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == Roles.TEACHER


class IsVerifiedStudentOrTeacher(IsAuthenticatedAndVerified):
    """
    Allows access only to authenticated Student or Teacher users with verified email.
    """
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role in [Roles.STUDENT, Roles.TEACHER]


class IsSuperAdminOrReadOnlyVerifiedStudentOrTeacher(IsAuthenticatedAndVerified):
    """
    - Full access: verified SuperAdmin
    - Read-only: verified Student or Teacher
    """
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False

        if request.user.role == Roles.SUPERADMIN:
            return True

        return request.method in SAFE_METHODS and request.user.role in [Roles.STUDENT, Roles.TEACHER]


class IsSuperAdmin(BasePermission):
    """
    Allows access to authenticated SuperAdmin only (no verified email check).
    """
    def has_permission(self, request, view):
        return getattr(request.user, "is_authenticated", False) and request.user.role == Roles.SUPERADMIN


class IsStudent(BasePermission):
    """
    Allows access to authenticated Student only (no verified email check).
    """
    def has_permission(self, request, view):
        return getattr(request.user, "is_authenticated", False) and request.user.role == Roles.STUDENT


class IsTeacher(BasePermission):
    """
    Allows access to authenticated Teacher only (no verified email check).
    """
    def has_permission(self, request, view):
        return getattr(request.user, "is_authenticated", False) and request.user.role == Roles.TEACHER
