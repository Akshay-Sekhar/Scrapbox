from django.contrib import admin

from scrapboxapp.models import User,Product,UserProfile

admin.site.register(Product)
admin.site.register(UserProfile)