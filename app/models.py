from django.db import models

# Create your models here.
class Brand(models.Model):
  brandName = models.CharField(max_length=100,primary_key=True)

class BikeInfo(models.Model):
  bikeName = models.CharField(max_length=100,primary_key=True)
  brandName = models.ForeignKey(Brand,on_delete=models.CASCADE) 
  price = models.IntegerField()
  url = models.URLField()
  
class CustomerInfo(models.Model):
  customerName = models.CharField(max_length=100,primary_key=True) 
  bikeName = models.ForeignKey(BikeInfo,on_delete=models.CASCADE)
  phoneNumber = models.IntegerField()
  