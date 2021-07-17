from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey

# Create your models here.

class products(models.Model):
    prod_name = models.CharField(max_length=30, primary_key= True)
    prod_price = models.IntegerField()
    prod_img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.prod_name

class buy_details(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=100)
    pincode= models.IntegerField()
    email = models.EmailField()
    prod_ordered = models.ForeignKey(products, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
