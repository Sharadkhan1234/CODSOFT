from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class main(models.Model):
	h = models.CharField(max_length=20)
	# def __str__(self):
	# 	return self.h

class category(models.Model):
	p =  models.ForeignKey(main,on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	brand = models.CharField(max_length=100)
	image = models.ImageField(upload_to="product")
	# def __str__(self):
	# 	return self.p



class sub_cat(models.Model):
	cat_name = models.ForeignKey(category,on_delete=models.CASCADE)
	name= models.CharField(max_length=100)
	brand= models.CharField(max_length=100)
	price= models.IntegerField()
	d1= models.CharField(max_length=100)
	d2= models.CharField(max_length=100)
	d3= models.CharField(max_length=100)
	d4= models.CharField(max_length=100)
	img= models.ImageField(upload_to="product")
	# def __str__(self):
	# 	return self.name




class product(models.Model):
	sub_name = models.ForeignKey(sub_cat,on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	price = models.IntegerField()
	brand = models.CharField(max_length=100)
	image = models.ImageField(upload_to="product")
	d1 = models.CharField(max_length=200)
	d2 = models.CharField(max_length=200)
	d3 = models.CharField(max_length=200)
	d4 = models.CharField(max_length=200)
	# 
# def __str__(self):
# 	# 	return self.name




class otp_model(models.Model):
	otp = models.IntegerField()
	number = models.IntegerField()
	datetime = models.DateTimeField()


# class User(AbstractUser):
# 	phone = models.IntegerField()
	


