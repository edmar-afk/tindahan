from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=250)
    status = models.CharField(max_length=100)
    price = models.IntegerField()
    type = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='images/')