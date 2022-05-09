from django.db.models.signals import post_save
from accounts.models import User

from .models import Profile


def create_user_profile(sender, **kwargs):
    if kwargs["created"]:
        if not kwargs["instance"].is_admin:
            p1 = Profile(user=kwargs["instance"])
            p1.save()


post_save.connect(sender=User, receiver=create_user_profile)
