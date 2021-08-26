from rest_framework import viewsets, status 
from .models import Product, Rating 
from django.contrib.auth.models import User 
from .serializers import ProductSerializer, RatingSerializer
from rest_framework.decorators import action 
from rest_framework.response import Response 



class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer 
    queryset = Product.objects.all() 

    # Extra Action for Rating Product
    @action(detail=True, methods=['POST'])
    def rating_product(self, request, pk=None):
        if 'stars' in request.data : 
            '''
                Create | Update the Rating 
            '''
            product = Product.objects.get(id=pk)
            user = User.objects.get(username = request.data['username']) 
            stars = request.data['stars']
            try:

                ####  Update the Rate 
                rating = Rating.objects.get(product=product, user=user.id)
                rating.stars = stars 
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                data = {
                    'Message' : 'Product Rating is Updated',
                    'result' : serializer.data 
                }
                return Response(data, status=status.HTTP_202_ACCEPTED)

            except:
                # Create if the product rate isn't set 
                rating = Rating.objects.create(product=product, user=user, stars=stars)
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                data = {
                    'Message' : 'Product Rating is Created',
                    'result' : serializer.data 
                }
                return Response(data, status=status.HTTP_201_CREATED)
        else :
            data = {
                'Message' : 'Stars Not Provided .... '
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)




class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()