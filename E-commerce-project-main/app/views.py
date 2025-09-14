from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse
from .models import*
from django.contrib.auth.models import User,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as l,logout
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
import random
import datetime
import socket  



# Create your views here.

def login(request):
	return render(request,'login.html')


def mainn(request):
	p = category.objects.all()
	head = main.objects.all()
	return render(request,'home.html',{'data':p,'data3': head })


def home(request,id):
	head = main.objects.all()
	h = category.objects.filter(p=id)
	return render(request,'home.html',{'data':h,'data3': head })


def sub(request,id):
	head = main.objects.all()
	c = sub_cat.objects.filter(cat_name=id)
	return render(request,'sub.html',{'data2':c,'data3': head })


def product_show(request,id):
	head = main.objects.all()
	d = product.objects.filter(sub_name=id)
	return render(request,'product.html',{'data2':d,'data3': head }) 

def header(request):
	return render(request,'header.html')

def payment(request):
	return render(request,'payment.html')



# def genrateotp():
# 	x = random.randint(1111,9999)
# 	return x

# class sub_category(serializers.ModelSerializer):
# 	class Meta:
# 		model = category
# 		fields = '__all__'



# class cat(APIView):
# 	def get(self,request):
# 		number = request.query_params['number']
# 		otp = genrateotp() 
# 		c = otp_model(otp=otp,number=number,)
# 		c.save()
# 		if c:
# 			return HttpResponse(otp)


def SignupPage(request):
	if request.method=='POST':
		uname = request.POST.get('username')
		email = request.POST.get('email')
		pass1 = request.POST.get('Password1')
		pass2 = request.POST.get('Password2')
		if pass1 != pass2:
			return HttpResponse("Your Password And Confirm Password Are Not Same !!")
		else:
			my_user = User.objects.create_user(uname,email,pass1)
			my_user.save()
			return redirect('login')
	return render(request,'signup.html')

def logout_view(request):
    logout(request)
    return redirect('login') 


def LoginPage(request):
	if request.method=='POST':
		username=request.POST.get('username')
		pass1=request.POST.get('pass')
		user=authenticate(request,username=username,password=pass1)
		if user is not None:
			l(request,user)
			return redirect('main')
		else:
			return HttpResponse("Username or Password Incorrect !!")
	return render(request,'login.html')
 



class pro(serializers.ModelSerializer):
	class Meta:
		model=product
		fields=['price']

class cat(APIView):
	def get(self,request):
		idd = request.query_params["idd"]
		q = request.query_params["q"]
		s = product.objects.get(id=idd)
		c = pro(s)
		price = s.price
		final = int(price) * int(q)

		return HttpResponse(final)


class c(serializers.ModelSerializer):
	class Meta:
		model=category
		fields=['name']

class search(APIView):
	def s(self,request):
		d = request.query_params['search']
		a = category.objects.get(name=d)
		a = c(a)
		return Response(a.data)






