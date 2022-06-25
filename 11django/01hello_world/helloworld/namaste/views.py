from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("Namaste is hello in India")
