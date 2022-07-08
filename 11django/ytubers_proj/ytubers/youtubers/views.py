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