
from django.db import models

from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Monitors(models.Model):
    title = models.CharField(max_length=50, default='no title')
    brand = models.CharField(max_length=20, default='brand not found')
    description = models.TextField()
    price = models.IntegerField()
    on_sale = models.BooleanField(default=False)
    featured_image_url = models.CharField(max_length=500, default='No image')
    image_urls = ArrayField(models.CharField(max_length=500, default='No image'), max_length=5)

    def __str__(self):
        return self.title


