from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Property(models.Model):
    title = models.CharField(max_length=200)
    description=models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='properties/')
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    message=models.TextField()

class Inquiry(models.Model):
    property=models.ForeignKey(Property,on_delete=models.CASCADE)
    location=models.CharField(max_length=200)
    budget=models.DecimalField(max_digits=10,decimal_places=2)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    
