from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=500)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    image = models.ImageField(upload_to='imgs/products/')
    
    # No.Rating 
    def no_of_ratings(self):
        ratings = Rating.objects.filter(product=self)
        return len(ratings)

    def avg_rating(self):
        # sum / no_of_ratings 
        sum = 0  # initial value Zero 
        ratings = Rating.objects.filter(product=self)
        for i in ratings :
            sum += i.stars 
        if sum > 0:
            return sum / len(ratings)
        else : 
            return 0


    def __str__(self):
        return self.name 
    class Meta:
        db_table = 'Products'


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'product'))
        index_together = (('user', 'product'))