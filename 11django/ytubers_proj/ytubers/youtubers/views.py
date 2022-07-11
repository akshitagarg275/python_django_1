from django.shortcuts import render
from .models import Youtuber
# Create your views here.

def youtubers(request):
    youtuber=Youtuber.objects.all()
    data={
        'youtuber':youtuber
    }
    return render(request,'youtubers/youtubers.html',data)


def single_youtuber(request, id):
    youtuber = Youtuber.objects.get(id = id)
    data={
        'youtuber':youtuber
    }
    return render(request , 'youtubers/single_youtuber.html' ,data)


def search(request):
    tubers=Youtuber.objects.order_by('-created_at')
    camera_search=Youtuber.objects.values_list('camera_type',flat=True).distinct()
    category_search =Youtuber.objects.values_list('category',flat=True).distinct()
    city_search=Youtuber.objects.values_list('city',flat=True).distinct().order_by('city')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
    
    tubers = tubers.filter(desc__contains=keyword)
    print(city_search)

    data = {
        'tubers': tubers,
        'camera_search':camera_search,
        'city_search':city_search,
        'category_search':category_search
    }
    print(data)

    return render(request, 'youtubers/search.html',data)

