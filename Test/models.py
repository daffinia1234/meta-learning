from django.db import models

# Create your models here.
types=[
    ('commercial','COMMERCIAL'),
    ('residential' ,'RESIDENTIAL')]
class Addproperty(models.Model):
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=50)
    price_per_sqft=models.FloatField()
