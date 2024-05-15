from django.db import models

class Dojo(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    desc=models.TextField(null=True)

class Ninja(models.Model):
    dojo_id=models.ForeignKey(Dojo,related_name='dojos', on_delete=models.CASCADE)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)