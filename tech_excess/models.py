
import email
from django.db import models

from django.contrib.postgres.fields import ArrayField
# Create your models here.
#https://www.youtube.com/watch?v=0d7cIfiydAc
#user tutorial
from django.contrib.auth.models import User

class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    total = models.IntegerField(default=0)
    order_completed = models.BooleanField(default=False)



class Wishlist(models.Model):
    name = models.CharField(max_length=50, default='Wishlist')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlists')

    def __str__(self):
        return self.name

class Item(models.Model):
    title = models.CharField(max_length=50, default='no title')
    brand = models.CharField(max_length=20, default='brand not found')
    category = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    on_sale = models.BooleanField(default=False)
    featured_image_url = models.CharField(max_length=500, default='No image')
    image_urls = ArrayField(models.CharField(max_length=500, default='No image'), max_length=5)
    wishlists = models.ManyToManyField(Wishlist, related_name='items')
    carts = models.ManyToManyField(Cart, related_name='items')

    def __str__(self):
        return self.title


class ItemReview(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100, default='Title here')
    body = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.title



