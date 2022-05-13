from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_extensions.db.models import TimeStampedModel
from helpers import get_file_path


# Create your models here.
class Product(TimeStampedModel):
    name = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    screen_size = models.FloatField()
    cpu_cache = models.FloatField()
    ram = models.FloatField()
    memory_capacity = models.FloatField()
    battery_description = models.CharField(max_length=500)
    count = models.PositiveIntegerField()
    image = models.ImageField(upload_to=get_file_path,blank=True)

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.slug = slugify(self.name)
        return super(Product, self).save()

    def get_absolute_url(self):
        pass
        # return reverse("products:detail", args=[self.name])
