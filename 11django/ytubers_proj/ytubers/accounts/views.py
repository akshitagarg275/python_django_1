from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator
# Create your views here.

def login(request):
    if request.method =='POST':
        userName=request.POST['userName']
        password=request.POST['password']
        user = auth.authenticate(username=userName , password=password)
        print(userName,password)
        print("user is :",user)
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
            if len(password) > 6 or len(password) <=12:
                if User.objects.filter(username = userName).exists():
                    messages.error(request,"User already exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstName,last_name=lastName,username=userName,email=email,password=password)
                    print(user)
                    user.save()
                    messages.success(request,"User created successfully")
                    return redirect('login')
            else:
                print("Password should be of length 6-10")
        else:
            messages.error(request,"Passwords do not match")
            return redirect('register')
    return render(request,'accounts/register.html')

def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
# @method_decorator(login_required(login_url='/accounts/login/'))
def dashboard(request):
    return render(request,'accounts/dashboard.html')