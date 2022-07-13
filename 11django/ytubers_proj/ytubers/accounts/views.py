from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth,messages
# Create your views here.

def login(request):
    if request.method =='POST':
        userName=request.POST['userName']
        password=request.POST['password']
        user = auth(username=userName , password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"User logged in successfully")
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('login')
    return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        userName = request.POST['userName']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        if password == confirmPassword:
            if len(password) > 6 and len(password<=10):
                if User.objects.filter(username = userName).exists():
                    messages.error(request,"User already exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstName,last_name=lastName,username=userName,email=email,password=password)
                    user.save()
                    messages.success(request,"User created successfully")
                    return redirect('login')
            else:
                print("Password should be of length 6-10")
        else:
            messages.error(request,"Passwords do not match")
            return redirect('register')
    return render(request,'accounts/register.html')


def dashboard(request):
    return render(request,'accounts/dashboard.html')