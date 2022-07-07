from django.shortcuts import render
from .models import Youtuber
# Create your views here.

def youtubers(request):
    youtuber=Youtuber.objects.all()
    data={
        'youtuber':youtuber
    }
    return render(request,'youtubers/youtubers.html',data)