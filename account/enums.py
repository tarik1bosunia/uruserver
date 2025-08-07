from django.db import models
from django.utils.translation import gettext_lazy as _


class Roles(models.TextChoices):
    SUPERADMIN = 'superadmin', _('Super Admin')
    STUDENT = 'student', _('Student')
    TEACHER = 'teacher', _('Teacher')
    

class AuthProvider(models.TextChoices):
    EMAIL = 'email', _('Email')
    GOOGLE = 'google', _('Google')
