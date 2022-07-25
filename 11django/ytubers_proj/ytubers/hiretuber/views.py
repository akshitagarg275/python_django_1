from django.shortcuts import render,redirect
from .models import Hiretuber
from django.contrib import messages
# Create your views here.

def hiretuber(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        user_id = request.POST['user_id']
        email = request.POST['email']
        tuber_name = request.POST['tuber_name']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        message = request.POST['message']
        ytuber_id = request.POST['ytuber_id']

        hiretuber = Hiretuber(first_name = fname ,last_name = lname , tuber_id = ytuber_id ,user_id = user_id,
                    tuber_name=tuber_name, city = city , state = state , email =email , phone=phone , message = message )
        print(hiretuber)
        hiretuber.save()
        print("SUCCESS")
        messages.success(request, 'Thanks for reaching out !')
        return redirect('youtubers')