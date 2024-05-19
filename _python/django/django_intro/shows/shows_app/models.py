from django.db import models
from django.utils import timezone

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show name should be at least two characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least three characters"
        if len(postData['desc'])<10:
            errors['desc']="Show description should be at least ten characters"
        return errors
    
class Show(models.Model):
    title=models.CharField(max_length=45)
    network=models.CharField(max_length=45)
    release_date=models.DateField()
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ShowManager()
