from django.shortcuts import render
from .models import Slider , Team
from youtubers.models import Youtuber
# Create your views here.

def home(request):
    sliders = Slider.objects.all()
    team = Team.objects.all()
    youtuber=Youtuber.objects.order_by('-created_at')
    ft_youtuber = Youtuber.objects.filter(is_featured=True)
    # print(sliders)
    data={
        'sliders':sliders,
        'team':team,
        'youtuber':youtuber,
        'ft_youtuber':ft_youtuber
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