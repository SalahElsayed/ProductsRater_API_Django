from rest_framework import viewsets  
from .models import Product, Rating 
from .serializers import ProductSerializer, RatingSerializer



class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer 
    queryset = Product.objects.all() 


class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()