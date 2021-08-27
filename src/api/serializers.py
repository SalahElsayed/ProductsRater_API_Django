from rest_framework import serializers
from .models import Product, Rating
from django.contrib.auth.models import User 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('username', 'password')
        extra_kwargs = {'password' : {'write_only' : True, 'required' : True}}


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'image', 'description', 'no_of_ratings', 'avg_rating')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating 
        fields = ('user', 'product', 'stars',)