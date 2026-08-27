from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def authlogin(request):
    if request.method == 'POST':
        name=request.POST['name']
        password=request.POST['password']
        user=authenticate(request,username = name, password = password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.error(request, "Username or Password invalid!")
    return render(request, 'authentication/login.html')

def authregistration(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password'] 
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Already Exist')
            else:
               User.objects.create_user(username=username,password=password)
              
               return redirect('profile')   

        else:
          messages.error(request,'Password & Confirm_Password not matched')
    return render(request, 'authentication/registration.html')

def forgotpassword(request):
    return render(request, 'authentication/forgot.html')

def userlogout(request):
    logout(request)
    messages.success(request, "Successfully Logout!")
    return redirect('login')