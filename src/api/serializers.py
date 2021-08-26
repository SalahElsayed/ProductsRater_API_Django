from rest_framework import serializers
from .models import Product, Rating

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'image', 'description', 'no_of_ratings', 'avg_rating')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating 
        fields = ('user', 'product', 'stars',)