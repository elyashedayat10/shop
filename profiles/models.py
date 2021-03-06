from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django_extensions.db.models import TimeStampedModel

from helpers import get_file_path

user_model = settings.AUTH_USER_MODEL


class Profile(TimeStampedModel):
    user = models.OneToOneField(
        user_model,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    image = models.ImageField(
        upload_to=get_file_path,
        blank=True,
    )
    full_name = models.CharField(
        max_length=255,
        blank=True,
    )
    email = models.EmailField(
        unique=True,
        blank=True,
    )
    receive_blog = models.BooleanField(default=False)
