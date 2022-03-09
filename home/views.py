import email
from email import message
from time import time
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from home.models import tablebook , contactus


# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method == "POST":
        if request.POST.get('name'):
            name = request.POST.get('name')
            email =request.POST.get('email')
            phone =request.POST.get('phone')
            date =request.POST.get('date')
            time =request.POST.get('time')
            people =request.POST.get('people')
            message =request.POST.get('message')
            object = tablebook(name= name,email =email,phone= phone,date= date,time= time,people= people,message=message)
            object.save()
            return render(request, 'index.html')

    if request.method == "POST":
        if request.POST.get('cname'):
            cname = request.POST.get('cname')
            email =request.POST.get('email')
            subject =request.POST.get('subject')
            message =request.POST.get('message')
            object2 = contactus(cname= cname,email= email,subject= subject,message= message)
            object2.save()
            return render(request, 'index.html')

    return render(request, 'index.html')

def loginuser(request):
    # check if user has enter correct creadintials
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(username= username, password= password)
        if user is not None:
        # A backend authenticated the credentials
            login(request,user)
            return redirect('/')
        else:
        # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")

def signup(request):
    if request.method =='POST': 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,f' hii {username} ,your account created successfully')
            return redirect('login')
            
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})
#vikas12345
