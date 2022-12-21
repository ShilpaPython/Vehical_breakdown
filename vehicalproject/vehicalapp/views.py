from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate

# Create your views here.

def index(request):
    return render (request,'vehcare.html')

def customersignup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        cnfpassword=request.POST['cnfpassword']

        if password==cnfpassword:
            if User.objects.filter(username=username):
                print('Username already exists')
                return redirect('/custsignup')
            elif User.objects.filter(email=email):
                print("email already exist")
                return redirect('/custsignup')
            else :
                User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)
                print('New user created successfully')
                return redirect('/customersignin')
        else:
            print("password does not matched") 
            return redirect('/custsignup')
    else:
        return render(request,'usersignup.html') 

def customersignin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print('user login successfully')
            return redirect('/')
        else:
            print('invalid creditials')
            return redirect('/customersignin')
    else:

        return render(request,'usersignin.html')        
