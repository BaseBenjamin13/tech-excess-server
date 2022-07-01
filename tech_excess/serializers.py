
from rest_framework import serializers
from .models import Monitors, KeyBoard, Mouse

class MonitorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Monitors
        fields = ('id', 'title', 'brand', 'description', 'price', 'on_sale', 'featured_image_url', 'image_urls',)

class KeyboardsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KeyBoard
        fields = ('id', 'title', 'brand', 'description', 'price', 'on_sale', 'featured_image_url', 'image_urls',)

class MousesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mouse
        fields = ('id', 'title', 'brand', 'description', 'price', 'on_sale', 'featured_image_url', 'image_urls',)



