
from rest_framework import serializers
from .models import Monitors

class MonitorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Monitors
        fields = ('id', 'title', 'brand', 'description', 'price', 'on_sale', 'image_url',)
