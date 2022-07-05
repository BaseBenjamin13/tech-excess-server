
from rest_framework import serializers
from .models import Monitors, KeyBoard, Mouse, HeadPhone, MonitorReview

class MonitorsSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        view_name='reviews_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Monitors
        fields = ('id', 'title', 'brand', 'description', 'price', 'on_sale', 'featured_image_url', 'image_urls', 'reviews',)

class KeyboardsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KeyBoard
        fields = ('id', 'title', 'brand', 'description', 'price', 'on_sale', 'featured_image_url', 'image_urls',)

class MousesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mouse
        fields = ('id', 'title', 'brand', 'description', 'price', 'on_sale', 'featured_image_url', 'image_urls',)

class HeadPhonesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HeadPhone
        fields = ('id', 'title', 'brand', 'description', 'price', 'on_sale', 'featured_image_url', 'image_urls',)

class MonitorReviewSerializer(serializers.HyperlinkedModelSerializer):
    monitor = serializers.HyperlinkedRelatedField(
        view_name='monitors_detail',
        many=False,
        read_only=True
    )
    class Meta:
        model = MonitorReview
        fields = ('monitor', 'author', 'body', 'rating',)

