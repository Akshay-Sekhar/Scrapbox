from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from scrapboxapp.models import Product,UserProfile

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"})) 
    
class ProductForm(forms.ModelForm):
    category = forms.ChoiceField(choices=Product.options, initial='others')
    class Meta:
        model=Product
        # fields="__all__"
        exclude=['owner']   
        
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "brand":forms.TextInput(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"}),
            "year":forms.TextInput(attrs={"class":"form-control"})   
            
        }   
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=('user',)
        
        widgets={
            "dob":forms.DateInput(attrs={"class":"form-control","type":"date"})
        }         
        