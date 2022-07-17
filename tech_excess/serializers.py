
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Item, ItemReview, Wishlist, Cart
from django.contrib.auth.models import User


class ItemsSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        view_name='reviews_detail',
        many=True,
        read_only=True
    )
    wishlists = serializers.HyperlinkedRelatedField(
        view_name='wishlists_detail',
        many=True,
        read_only=False, 
        queryset = Wishlist.objects.all()
    )
    carts = serializers.HyperlinkedRelatedField(
        view_name='carts_detail',
        many=True,
        read_only=False, 
        queryset = Cart.objects.all()
    )
    class Meta:
        model = Item
        fields = ('id', 'title', 'brand', 'category', 'description', 'price', 'on_sale', 'featured_image_url', 'image_urls', 'wishlists', 'reviews', 'carts',)


class ItemReviewSerializer(serializers.HyperlinkedModelSerializer):
    item = serializers.HyperlinkedRelatedField(
        view_name='items_detail',
        many=False,
        read_only=False, 
        queryset = Item.objects.all()
    )
    author = serializers.ReadOnlyField(
        source='author.username'
    )
    class Meta:
        model = ItemReview
        fields = ('id', 'item', 'author', 'title', 'body', 'rating',)

class WishlistSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedRelatedField(
        view_name='items_detail',
        many=True,
        read_only=False, 
        queryset = Item.objects.all()
    )
    owner = serializers.ReadOnlyField(
        source='owner.username'
    )
    class Meta:
        model = Wishlist
        fields = ('id', 'name', 'owner', 'items',)


class CartSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedRelatedField(
        view_name='items_detail',
        many=True,
        read_only=False, 
        queryset = Item.objects.all()
    )
    owner = serializers.ReadOnlyField(
        source='owner.username'
    )
    class Meta:
        model = Cart
        fields = ('id', 'owner', 'total', 'items',)






