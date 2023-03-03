from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     deo=models.BooleanField(default=False)
#     #fac=models.BooleanField(default=False)
    


class Stock(models.Model):  
    # User= settings.AUTH_USER_MODEL
    user= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    sid = models.CharField(max_length=20)  
    sname = models.CharField(max_length=100)  
    squantity = models.IntegerField()  
    class Meta:  
        db_table = "stock"  
        