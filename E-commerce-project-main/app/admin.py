from django.contrib import admin
from .models import*
from django.contrib.auth.admin import User
# from .models import User 



# Register your models here.

admin.site.register([category,sub_cat,product,main])