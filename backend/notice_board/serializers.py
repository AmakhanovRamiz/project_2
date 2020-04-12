from rest_framework import serializers

from backend.gallery.serializers import GallerySer
from .models import *

class CategorytSer(serializers.ModelSerializer):
    """Для вывода категорий"""
    class Meta:
        model = Category
        fields = ('name', )


class FilterAdvertSer(serializers.ModelSerializer):
    """Для вывода фильтров"""
    class Meta:
        model = Category
        fields = ('name', )

class AdvertListSer(serializers.ModelSerializer):
    """Для вывода списка объявлений"""
    category = CategorytSer()
    filters = FilterAdvertSer()
    images = GallerySer(read_only = True)

    class Meta:
        model = Advert
        fields = ('id', 'category', 'filters', 'subject', 'images', 'price', 'created', 'slug')


class AdvertDetailSer(serializers.ModelSerializer):
    """Для вывода полного объявления"""
    category = CategorytSer()
    filters = FilterAdvertSer()
    images = GallerySer(read_only = True)

    class Meta:
        model = Advert
        fields = (
            'category', 
            'filters', 
            'subject', 
            'description', 
            'file', 
            'images', 
            'price', 
            'created',
            'user'
            )

class AdvertCreateSer(serializers.ModelSerializer):
    """Добавление объявления"""

    class Meta:
        model = Advert
        fields = (
            'category', 
            'filters',
            'date', 
            'subject', 
            'description', 
            'price', 
            )
        
        def create(self, request):
            request['user'] = self.context['request'].User
            advert = Advert.objects.update_or_create(**request)
            return advert