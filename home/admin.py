from django.contrib import admin

# Register your models here.
from django.contrib import admin
from home.models import  Address, Cart, Contact, Orders,Products
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Contact)
# admin.site.register(User)
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(Address)