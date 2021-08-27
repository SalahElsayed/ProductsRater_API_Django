from rest_framework import serializers, viewsets, status 
from .models import Product, Rating 
from django.contrib.auth.models import User 
from .serializers import ProductSerializer, RatingSerializer, UserSerializer 
from rest_framework.decorators import action 
from rest_framework.response import Response 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token 


# Viewset for only creating users 
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all() 
    permission_classes = (AllowAny, )


    # Create & Returning Token Token 
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance) # Create Token 
        return Response(
            {'token' : token.key }, status = status.HTTP_201_CREATED # Return token 
        )

    # List unauthorized 
    def list(self, request, *args, **kwargs):
        response = {
            'message' : 'operation not provided'
            }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    # delete unauthorized 
    def delete(self, request, *args, **kwargs):
        response = {
            'message' : 'operation not provided'
            }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    # put unauthorized 
    def put(self, request, *args, **kwargs):
        response = {
            'message' : 'operation not provided'
            }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    # retrieve unauthorized 
    def retrieve(self, request, *args, **kwargs):
        response = {
            'message' : 'operation not provided'
            }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    


# Product Viewset 
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer 
    queryset = Product.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
 

    # Extra Action for Rating Product
    @action(detail=True, methods=['POST'])
    def rating_product(self, request, pk=None):
        if 'stars' in request.data : 
            '''
                Create | Update the Rating 
            '''
            product = Product.objects.get(id=pk)
            user = request.user 
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
                return Response(data, status=status.HTTP_200_OK)

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
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        data = {
            'message' : "Invalid way to create .... "
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = {
            'message' : "Invalid way to update .... "
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)