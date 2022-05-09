from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(
        max_length=11,
        validators=[RegexValidator(r"^09[0|1|2|9][0-9]{8}$")],
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"

    objects = UserManager()

    def __str__(self):
        return self.phone_number

    @property
    def is_staff(self):
        return self.is_admin
