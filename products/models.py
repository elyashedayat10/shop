from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.core.validators import MaxValueValidator
from django.urls import reverse


# Create your models here.
class Product(TimeStampedModel):
    name = models.CharField(max_length=500)
    description = models.TextField()
    screen_size = models.PositiveIntegerField(MaxValueValidator(100))
    cpu_cache = models.PositiveIntegerField(MaxValueValidator(24))
    ram = models.PositiveIntegerField(MaxValueValidator(48))
    memory_capacity = models.PositiveIntegerField(MaxValueValidator(1024))
    battery_description = models.CharField(max_length=500)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass
        # return reverse("products:detail", args=[self.name])
