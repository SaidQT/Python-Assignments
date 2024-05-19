from django.db import models

class Actor(models.Model):
    name=models.CharField(max_length=45)
    
class Category(models.Model):
    name=models.CharField(max_length=45)
    
    
class Director(models.Model):
    name=models.CharField(max_length=45)
    
class Movie(models.Model):
    Title=models.CharField(max_length=45)
    Description=models.TextField()
    url_image=models.TextField()
    Category=models.ForeignKey(Category,related_name="movies",on_delete=models.CASCADE)
    Actors=models.ManyToManyField(Actor,related_name="movies")
    Director=models.ForeignKey(Director,related_name="director",on_delete=models.CASCADE,null=True)
