from django.shortcuts import render,redirect,reverse
from django.views.generic import CreateView,FormView,TemplateView, DetailView, View, UpdateView
from django.contrib import messages 
from django.contrib.auth import logout,authenticate,login
from django.utils.decorators import method_decorator

from scrapboxapp.forms import RegistrationForm,LoginForm,ProductForm,UserProfileForm
from scrapboxapp.models import Product,UserProfile,Basket,BasketItem

# Create your views here.

def signin_required(fn):
    def wrapper(request,*args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"Invalid session")
            return redirect("signin")
        else:
            return fn(request,*args, **kwargs)
    return wrapper 
            

class SignUpView(CreateView):
    template_name="register.html"
    form_class=RegistrationForm
    
    def get_success_url(self):
        return reverse("signin")
      
  
class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm    
    
    def post(self,request,*args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                login(request,user_object)
                return redirect("home")
            
        messages.error(request,"Login failed, invalid credentials")
        return render(request,"login.html",{"form":form}) 

@method_decorator(signin_required,name="dispatch")    
class HomeView(TemplateView):
    template_name="home.html"    

@method_decorator(signin_required,name="dispatch")    
class ProductView(TemplateView):
    template_name="products.html" 

@method_decorator(signin_required,name="dispatch")        
class ProductCreateView(View):
    def get(self,request,*args, **kwargs):
        
        form=ProductForm()
        
        return render(request,"product_add.html",{"form":form})
    
    def post(self,request,*args, **kwargs):
        
        form=ProductForm(request.POST,files=request.FILES)
        
        if form.is_valid(): 
            
            form.instance.owner=request.user
            
            form.save()
            
            messages.success(request,"Product created successfully")
            
            return redirect("productlist")
        
        else:
            
            messages.error(request,"failed to create product")
            
            return render(request,"product_add.html",{"form":form})   
        

@method_decorator(signin_required,name="dispatch")        
class CarsView(View):
    
    def get(self,request,*args, **kwargs):
        qs=Product.objects.filter(category="car")
        return render(request,"carlist.html",{"data":qs})
        
        
@method_decorator(signin_required,name="dispatch")        
class BikesView(View):
    
    def get(self,request,*args, **kwargs):
        qs=Product.objects.filter(category="bike")
        return render(request,"bikelist.html",{"data":qs})


@method_decorator(signin_required,name="dispatch")    
class MobilesView(View):
    
    def get(self,request,*args, **kwargs):
        qs=Product.objects.filter(category="mobile")
        return render(request,"mobilelist.html",{"data":qs})
    
    
@method_decorator(signin_required,name="dispatch")    
class OtherProductsView(View):  
    
    def get(self,request,*args, **kwargs):
        qs=Product.objects.filter(category="others")
        return render(request,"otherslist.html",{"data":qs})
 
    
@method_decorator(signin_required,name="dispatch")       
class ProductDetailView(View):
    
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Product.objects.get(id=id)
        return render(request,"product_detail.html",{"data":qs})

@method_decorator(signin_required,name="dispatch")        
class ProductUpdateView(View):
    
    def get(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        obj=Product.objects.get(id=id)
        
        form=ProductForm(instance=obj)
        
        return render(request,"product_edit.html",{"form":form})    
    
    def post(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        obj=Product.objects.get(id=id) 
        
        form=ProductForm(request.POST,instance=obj,files=request.FILES)
        
        
        if form.is_valid():
            
            if form.instance.owner==request.user:
            
                form.save()
            
                messages.success(request,"Product updated successfully")
            
                return redirect("productlist")
            
            else:
                
                messages.error(request,"You are not authorized to delete the product")
            
                return render(request,"product_edit.html",{"form":form}) 
        
        else:
            
            messages.error(request,"Failed to update product")
            
            return render(request,"product_edit.html",{"form":form})     
        


@method_decorator(signin_required,name="dispatch")            
class ProductDeleteView(View):
    def get(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")     
        
        product=Product.objects.get(id=id)
        
        if request.user==product.owner:
            
            product.delete()
        
            messages.success(request,"Product deleted successfully")
        
            return redirect("productlist")
        
        else:
            
            
            messages.error(request,"You are not authorized to delete the product")
            
            return redirect("productlist")          
        
          
@method_decorator(signin_required,name="dispatch")        
class SignOutView(View):
    def get(self,request,*args, **kwargs):
        logout(request)
        return redirect("signin") 
    
@method_decorator(signin_required,name="dispatch")            
class ProfileDetailView(DetailView):
    template_name="profile_detail.html"
    model=UserProfile
    context_object_name="data"
    
    
@method_decorator(signin_required,name="dispatch")            
class ProfileUpdateView(UpdateView):
    template_name="profile_edit.html"
    form_class=UserProfileForm
    model=UserProfile
        
    def get_success_url(self):
        return reverse("profile-detail",kwargs={'pk': self.object.pk})    
    

class AddToCartView(View) :
    
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Product.objects.get(id=id)
        return render(request,"scrapboxitem_view.html",{"data":qs})
    
    def add_to_cart(self,request,*args,**kwargs):
                id=kwargs.get("pk")
                product=Product.objects.get(id=id)
                cart,created=Basket.objects.get_or_create(user=request.user)
                cart_item,item_created = BasketItem.objects.get_or_create(cart=cart,product=product)
                if not item_created:
                         cart_item.quantity += 1
                         cart_item.save()
    
                return redirect("index")
            
class CartListView(View):
    def get(self,request,*args,**kwargs):
        qs=Basket.objects.all()
        return render(request,"cartlist.html",{"data":qs})            
            
             
            
    