from django.contrib.messages.api import debug
from django.db import models

# Create your models here.
from django.db.models.base import Model
from Ecommerce.settings import STATICFILES_DIRS, STATIC_URL
from datetime import date
from django.db import models
from django.conf import settings
from django.conf.urls.static import static
import datetime
import uuid
from django.contrib.auth.models import User
# from django.db import migrations


# class User(models.Model):
#   name=models.CharField(max_length=20)
#   email=models.EmailField(max_length=25,primary_key=True,null=False)
#   password=models.CharField(max_length=15)
  
#   def __str__(self) :
#       return self.name

class Contact(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
      return self.name


class Products(models.Model):
  product_name=models.CharField(max_length=100,primary_key=True)
  product_desc=models.CharField(max_length=500,null=True)
  product_price=models.IntegerField(default=0)
  product_img=models.FileField()
  product_img2=models.FileField(null=True)
  product_img3=models.FileField(null=True)
  
  def __str__(self) :
      return self.product_name 
 
# user=models.ForeignKey(User,default=1,on_delete=models.CASCADE)

class Cart(models.Model):
  user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
  product_name=models.CharField(max_length=100,primary_key=True)
  product_price=models.IntegerField(default=0)
  product_img=models.FileField()
  quantity=models.IntegerField(default=1)
  total_price= models.IntegerField(default=0)  
  def __str__(self) :
      return self.product_name

class Orders(models.Model):
  product_name=models.CharField(max_length=100,primary_key=True)
  product_price=models.IntegerField(default=0)  
  product_img=models.FileField()
  quantity=models.IntegerField(default=1)
  total_price= models.IntegerField(default=0)  
  def __str__(self) :
      return self.product_name

class Address(models.Model):
  username=models.CharField(max_length=20,primary_key=True)
  phone_number=models.IntegerField(null=False)
  address=models.CharField(max_length=150)
  pin=models.IntegerField(null=False)
  
  def __str__(self) :
      return self.username

  
