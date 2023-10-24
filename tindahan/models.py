from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=250)
    status = models.CharField(max_length=100)
    price = models.IntegerField()
    type = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='images/')
    

class Orders(models.Model):
    custname = models.ForeignKey(User, on_delete=models.CASCADE)
    oname = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(upload_to='profilePic/')