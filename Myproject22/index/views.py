from django.shortcuts import render
from .models import About
from .models import Slider


def home (request):
    aboutdata=About.objects.all()
    sliderdata=Slider.objects.all()
    context= {
        'about':aboutdata,
        'slider':sliderdata
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def profile(request):
    return render(request,'profile.html')