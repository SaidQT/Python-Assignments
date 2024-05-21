
from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name description should be at least 2 characters"
        if len(postData['email'])<0:
            errors['email']='Email is required'
        if len(postData['password'])<8:
            errors['password']="Password must be longer than 8 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):               
            errors['email'] = "Invalid email address!"
        if postData['password'] != postData['confirm_password']:
            errors['password']="Passwords don't match"
        return errors
    
class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if not postData['title']:
            errors["title"] = "Title is required"
        if len(postData['desc']) <5:
            errors["desc"] = "Description is required"
        return errors
    
class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    password=models.CharField(max_length=23)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
    
class Book(models.Model):
    title=models.CharField(max_length=45)
    desc=models.TextField()
    favorites=models.ManyToManyField(User,related_name='book_favorites')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    uploaded_by=models.ForeignKey(User,related_name='books',on_delete=models.CASCADE)
    objects=BookManager()