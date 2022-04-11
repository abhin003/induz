from django.db import models

# Create your models here.

class first_tb(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
class register_tb(models.Model):
    address_dr = models.CharField(max_length=200)
    state_dr = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)


class img_tb(models.Model):
	image = models.ImageField(upload_to='images')  
	picture = models.ImageField(upload_to='picture')  

class fav_steel(models.Model):
    fav_steel_u= models.CharField(max_length=200)
    userid=models.ForeignKey(first_tb,on_delete=models.CASCADE)
