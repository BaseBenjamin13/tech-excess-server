
from rest_framework import serializers
from .models import Item, ItemReview

class ItemsSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        view_name='reviews_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Item
        fields = ('id', 'title', 'brand', 'category', 'description', 'price', 'on_sale', 'featured_image_url', 'image_urls', 'reviews',)

# class KeyboardsSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = KeyBoard
#         fields = ('id', 'title', 'brand', 'description', 'price', 'on_sale', 'featured_image_url', 'image_urls',)

# class MousesSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Mouse
#         fields = ('id', 'title', 'brand', 'description', 'price', 'on_sale', 'featured_image_url', 'image_urls',)

# class HeadPhonesSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = HeadPhone
#         fields = ('id', 'title', 'brand', 'description', 'price', 'on_sale', 'featured_image_url', 'image_urls',)

class ItemReviewSerializer(serializers.HyperlinkedModelSerializer):
    item = serializers.HyperlinkedRelatedField(
        view_name='items_detail',
        many=False,
        read_only=False, 
        queryset = Item.objects.all()
    )
    class Meta:
        model = ItemReview
        fields = ('id', 'item', 'author', 'body', 'rating',)

