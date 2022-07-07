
import email
from django.db import models

from django.contrib.postgres.fields import ArrayField
# Create your models here.
#https://www.youtube.com/watch?v=0d7cIfiydAc
#user tutorial
from django.contrib.auth.models import User


class Item(models.Model):
    title = models.CharField(max_length=50, default='no title')
    brand = models.CharField(max_length=20, default='brand not found')
    category = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    on_sale = models.BooleanField(default=False)
    featured_image_url = models.CharField(max_length=500, default='No image')
    image_urls = ArrayField(models.CharField(max_length=500, default='No image'), max_length=5)

    def __str__(self):
        return self.title


class ItemReview(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=50, default='unknown')
    body = models.TextField()
    rating = models.IntegerField()
    #https://www.youtube.com/watch?v=0d7cIfiydAc
    #user tutorial  
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=True)

    def __str__(self):
        return self.author



# class KeyBoard(models.Model):
#     title = models.CharField(max_length=50, default='no title')
#     brand = models.CharField(max_length=20, default='brand not found')
#     description = models.TextField()
#     price = models.IntegerField()
#     on_sale = models.BooleanField(default=False)
#     featured_image_url = models.CharField(max_length=500, default='No image')
#     image_urls = ArrayField(models.CharField(max_length=500, default='No image'), max_length=5)

#     def __str__(self):
#         return self.title

# class Mouse(models.Model):
#     title = models.CharField(max_length=50, default='no title')
#     brand = models.CharField(max_length=20, default='brand not found')
#     description = models.TextField()
#     price = models.IntegerField()
#     on_sale = models.BooleanField(default=False)
#     featured_image_url = models.CharField(max_length=500, default='No image')
#     image_urls = ArrayField(models.CharField(max_length=500, default='No image'), max_length=5)

#     def __str__(self):
#         return self.title

# class HeadPhone(models.Model):
#     title = models.CharField(max_length=50, default='no title')
#     brand = models.CharField(max_length=20, default='brand not found')
#     description = models.TextField()
#     price = models.IntegerField()
#     on_sale = models.BooleanField(default=False)
#     featured_image_url = models.CharField(max_length=500, default='No image')
#     image_urls = ArrayField(models.CharField(max_length=500, default='No image'), max_length=5)

#     def __str__(self):
#         return self.title



