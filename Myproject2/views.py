
from django.http import HttpResponse

def home(request):
    data = "This is our home page"
    return HttpResponse(data)
def about(request):
    data = "This is our about page"
    return HttpResponse(data)
def contact(request):
    data = "This is our contact page"
    return HttpResponse(data)

