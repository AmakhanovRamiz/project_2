from rest_framework import serializers0

from . import models

class AdvertSer(serializers.ModelSerializer):
    """Для вывода объявлений"""
    class Meta:
        model = Advert
        fields = ('category', 'filters', 'subject', 'images', 'price', 'created')