from django.shortcuts import render

def home(request):
    text = {
        "name": "Auvishek Das",
        "address": "Dhaka",
        "phone": "254878"
    }
    return render(request,'index.html',text)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def profile(request):
    return render(request,'profile.html')