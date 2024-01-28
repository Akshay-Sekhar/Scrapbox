from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    address=models.CharField(max_length=200,null=True)
    location=models.CharField(max_length=200,null=True)
    dob=models.DateField(null=True)
    phone=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.user.username
    
def create_profile(sender,created,instance,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        
post_save.connect(create_profile,sender=User)   


class Product(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    brand=models.CharField(max_length=200)
    options=(
        ("car","car"),
        ("bike","bike"),
        ("mobile","mobile"),
        ("others","others")
    )    
    category=models.CharField(max_length=200,choices=options,default="others")
    location=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=200,null=True)
    year=models.TextField(null=True)
    picture=models.ImageField(upload_to="images",null=True,blank=True)
    
    def __str__(self):
        
        return self.name
    
  
    
    
         

