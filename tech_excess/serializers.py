
from rest_framework import serializers
from .models import Monitors

class MonitorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Monitors
        fields = ('id', 'title', 'brand', 'description', 'price', 'on_sale', 'featured_image_url', 'image_urls',)
