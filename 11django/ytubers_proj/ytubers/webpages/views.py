from django.shortcuts import render
from .models import Slider , Team
# Create your views here.

def home(request):
    sliders = Slider.objects.all()
    team = Team.objects.all()
    # print(sliders)
    data={
        'sliders':sliders,
        'team':team
    }
    return render (request , 'webpages/main.html',data)

def contact(request):
    return render (request , 'webpages/contact.html')

def about(request):
    return render (request , 'webpages/about.html')

def services(request):
    return render (request , 'webpages/services.html')

def dashboard(request):
    return render (request , 'webpagesdashboard/.html')