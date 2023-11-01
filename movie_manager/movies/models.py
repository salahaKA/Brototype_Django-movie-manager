from django.db import models

# Create your models here.
class MovieInfo(models.Model):
    name= models.CharField(max_length= 250)
    year= models.IntegerField(null=True)
    origin= models.TextField()
    poster= models.ImageField(upload_to= 'images/', null=True)
    
class Director(models.Model):
    name= models.CharField(max_length=300)



