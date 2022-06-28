
from django.db import models

# Create your models here.


class Monitors(models.Model):
    title = models.CharField(max_length=50, default='no title')
    brand = models.CharField(max_length=20, default='brand not found')
    description = models.TextField()
    price = models.IntegerField()
    on_sale = models.BooleanField(default=False)
    image_url = models.CharField(max_length=500, default='No image')

    def __str__(self):
        return self.title


