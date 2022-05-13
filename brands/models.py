from django.db import models
from django.utils.text import slugify
from helpers import get_file_path


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=125)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=get_file_path)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)
