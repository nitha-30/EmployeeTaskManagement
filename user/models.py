from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import _user_has_perm, _user_has_module_perms

from user.custom_managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(max_length=120, null=True, blank=True,
                              unique=True)
    phone_number = models.CharField(max_length=20)
    name = models.CharField(max_length=150, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        if self.is_superuser:
            return True
        return _user_has_perm(self, perm, obj)

    def has_module_perms(self, app_label):
        if self.is_superuser:
            return True
        return _user_has_module_perms(self, app_label)
