from django.shortcuts import render,redirect
from .models import About
from .models import Slider
from .models import Client
from .models import Contact

def home (request):
    aboutdata=About.objects.all()
    sliderdata=Slider.objects.all()
    clientdata=Client.objects.all()
    context= {
        'about':aboutdata,
        'slider':sliderdata,
        'client':clientdata
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            Contact.objects.create(name=name, email=email, message=message)

            return redirect('contact')

    return render(request,'contact.html')

def profile(request):
    return render(request,'profile.html')