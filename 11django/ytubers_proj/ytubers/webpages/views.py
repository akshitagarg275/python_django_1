from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request , 'webpages/main.html')

def contact(request):
    return render (request , 'webpages/contact.html')

def about(request):
    return render (request , 'webpages/about.html')

def services(request):
    return render (request , 'webpages/services.html')

def dashboard(request):
    return render (request , 'webpagesdashboard/.html')