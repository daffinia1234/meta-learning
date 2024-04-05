from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

types=[
    ('commercial','COMMERCIAL'),
    ('residential' ,'RESIDENTIAL')]

class NewProperty(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    location=models.CharField(max_length=50)
    total_area=models.FloatField()
    price_per_sqft=models.FloatField()
    property_type=models.CharField(max_length=20, choices=types)
    posted_date=models.DateField(auto_now=True)
    contact=models.IntegerField()

class Person(models.Model):
    name = models.CharField(max_length=50)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bonus=models.IntegerField(default=500)




    