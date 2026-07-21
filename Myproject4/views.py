from django.http import HttpResponse

def main_home(request):
    return HttpResponse("This is our Main module home page")
def profile(request):
    return HttpResponse("My Profile Page")
