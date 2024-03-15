from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import datetime
from django.utils import timezone

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
    
    
class Basket(models.Model):     #cart
    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="cart")
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    @property
    def cart_items(self):
        qs=self.cartitem.all() #cartitem points to basket of basketitem
        return qs    
    
class BasketItem(models.Model):     #cartitem
    basket=models.ForeignKey(Basket,on_delete=models.CASCADE,related_name="cartitem")
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.PositiveIntegerField(default=1)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    @property
    def total(self):
        return self.qty * self.product.price    
    
  
    
    
         

