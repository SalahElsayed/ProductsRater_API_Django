from django.conf.urls import url
from django.db.models import base
from django.urls import path 
from .views import ProductViewSet, RatingViewSet
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('ratings', RatingViewSet)


urlpatterns=[]

urlpatterns += router.urls 

