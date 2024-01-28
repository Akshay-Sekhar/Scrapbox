"""
URL configuration for scrapboxapplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from scrapboxapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',views.SignUpView.as_view(),name='signup'),
    path('login',views.SignInView.as_view(),name='signin'),
    path('logout',views.SignOutView.as_view(),name='signout'),
    path('home',views.HomeView.as_view(),name='home'),
    path('products',views.ProductView.as_view(),name='productlist'),    
    path('products/cars',views.CarsView.as_view(),name='carlist'),
    path('products/bikes',views.BikesView.as_view(),name='bikelist'),
    path('products/mobiles',views.MobilesView.as_view(),name='moblist'),
    path('products/others',views.OtherProductsView.as_view(),name='otherslist'),
    path('products/add',views.ProductCreateView.as_view(),name="product-add"),
    path('products/<int:pk>/detail',views.ProductDetailView.as_view(),name="product-detail"),
    path('products/<int:pk>/update',views.ProductUpdateView.as_view(),name="product-edit"),
    path('products/<int:pk>/delete',views.ProductDeleteView.as_view(),name="product-delete"),
    path('profile/<int:pk>',views.ProfileDetailView.as_view(),name="profile-detail"),
    path('profile/<int:pk>/change',views.ProfileUpdateView.as_view(),name="profile-update"),   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
