from django.db import models

# Create your models here.


class Users(models.Model):  
    Username = models.CharField(max_length=100)  
    First_name = models.CharField(max_length=100) 
    Last_name = models.CharField(max_length=100)   
    email = models.EmailField()   
    class Meta:
        db_table = "User"
    
